@Library('jenkins-shared-libraryy') _

pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        AWS_CREDS = 'aws-creds'
        LAMBDA_FUNCTION = 'hello_world_lambda'
        S3_BUCKET = 'bucket-new-9164'
        ARTIFACT_PATH = 'build/myfunction.zip'
        S3_KEY = 'myfunction.zip'
        ECS_CLUSTER = 'jenkins-cluster'
        ECS_SERVICE = 'jenkins-service'
        ECS_IMAGE = 'komalgt/myimage:latest'
    }

    stages {

        stage('Build Lambda Artifact') {
            steps {
                // Insert your build steps here, for example:
                // sh 'zip -j build/myfunction.zip src/main.py'
                echo "Building Lambda artifact as ${env. ARTIFACT_PATH}"
            }
        }

        stage('Upload Lambda Artifact to S3') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDS]]) {
                    sh """
                        aws s3 cp ${env. ARTIFACT_PATH} s3://${env.S3_BUCKET}/${env.S3_KEY} --region ${env.AWS_REGION}
                    """
                }
            }
        }

        stage('Lambda Deploy') {
            steps {
                deployLambda(
                    functionName: env.LAMBDA_FUNCTION,
                    s3Bucket: env.S3_BUCKET,
                    s3Key: env.S3_KEY,
                    awsRegion: env.AWS_REGION,
                    awsCredentialsId: env.AWS_CREDS
                )
            }
        }

        stage('ECS Deploy') {
            steps {
                deployECS(
                    cluster: env.ECS_CLUSTER,
                    service: env.ECS_SERVICE,
                    image: env.ECS_IMAGE,
                    awsRegion: env.AWS_REGION,
                    awsCredentialsId: env.AWS_CREDS
                )
            }
        }
    }
}
