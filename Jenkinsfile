@Library('jenkins-shared-libraryy') _

pipeline {
    agent any

    environment {
        S3_BUCKET = 'bucket-new-9164'
        S3_KEY    = 'myfunction.zip'
        REGION    = 'eu-north-1'
        LAMBDA_FUNCTION_NAME = 'my-lambda-func'
        // Add these as needed for ECS
        ECS_CLUSTER_NAME = 'my-ecs-cluster'
        ECS_SERVICE_NAME = 'my-ecs-service'
        IMAGE_TAG        = 'latest'
    }

    stages {
        stage('Checkout Source') {
            steps {
                checkout scm
                sh 'ls -alR'
            }
        }

        stage('Build Lambda Artifact') {
            steps {
                sh 'mkdir -p build'
                sh 'zip -r build/myfunction.zip lambda_function_code/lambda_function.py'
                sh 'ls -lh build/'
            }
        }

        stage('Upload Lambda Artifact to S3') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']
                ]) {
                    sh '''
                        ls -lh build/myfunction.zip
                        aws s3 cp build/myfunction.zip s3://$S3_BUCKET/$S3_KEY --region $REGION
                    '''
                }
            }
        }

        stage('Lambda Deploy') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']
                ]) {
                    sh '''
                        echo "Updating Lambda function code from S3..."
                        aws lambda update-function-code \
                            --function-name $LAMBDA_FUNCTION_NAME \
                            --s3-bucket $S3_BUCKET \
                            --s3-key $S3_KEY \
                            --region $REGION
                    '''
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                // Calls your shared library method (adjust params below as your ECSDeployer requires)
                script {
                    org.example.ECSDeployer.deployToECS(
                        cluster: env.ECS_CLUSTER_NAME,
                        service: env.ECS_SERVICE_NAME,
                        imageTag: env. IMAGE_TAG,
                        region: env.REGION,
                        awsCreds: 'aws-creds'
                    )
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed, please check earlier logs.'
        }
        always {
            cleanWs()
        }
    }
}
