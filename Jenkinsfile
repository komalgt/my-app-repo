@Library('jenkins-shared-libraryy') _

pipeline {
    agent any

    environment {
        S3_BUCKET = 'bucket-new-9164'
        S3_KEY    = 'myfunction.zip'
        REGION    = 'eu-north-1'
        LAMBDA_FUNCTION_NAME = 'my-lambda-func'
        ARTIFACT_PATH = 'build/myfunction.zip'
        ECS_CLUSTER_NAME = 'my-ecs-cluster'
        ECS_SERVICE_NAME = 'my-ecs-service'
        IMAGE = 'myrepo/myimage:latest'
        AWS_CREDENTIALS_ID = 'aws-creds'
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
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: "${env.AWS_CREDENTIALS_ID}"
                ]]) {
                    sh """
                        aws s3 cp ${env. ARTIFACT_PATH} s3://${env.S3_BUCKET}/${env.S3_KEY} --region ${env.REGION}
                    """
                }
            }
        }

        stage('Lambda Deploy (shared lib)') {
            steps {
                script {
                    // Adjust this if your shared lib function signature is different!
                    def lambda = new org.example.LambdaDeployer(this)
                    lambda.deploy(
                        functionName: env.LAMBDA_FUNCTION_NAME,
                        s3Bucket: env.S3_BUCKET,
                        s3Key: env.S3_KEY,
                        awsRegion: env.REGION,
                        awsCredentialsId: env.AWS_CREDENTIALS_ID
                    )
                }
            }
        }

        // ECS deploy stage (optional, example stub)
        stage('Deploy to ECS (shared lib)') {
            when {
                expression { false } // set to true if you have ECS deploy logic
            }
            steps {
                echo "ECS deploy step placeholder"
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
