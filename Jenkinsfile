@Library('jenkins-shared-libraryy') _

pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        AWS_CREDS = 'aws-creds'
        LAMBDA_FUNCTION = 'hello_world_lambda'
        S3_BUCKET = 'bucket-new-9164'
        ARTIFACT_PATH = 'build/myfunction.zip'
        ECS_CLUSTER = 'jenkins-cluster'
        ECS_SERVICE = 'jenkins-service'
        ECS_IMAGE = 'komalgt/myimage:latest'
    }

    stages {
        stage('Lambda Deploy') {
            steps {
                deployLambda(
                    functionName: env.LAMBDA_FUNCTION,
                    s3Bucket: env.S3_BUCKET,
                    artifactPath: env. ARTIFACT_PATH,
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
