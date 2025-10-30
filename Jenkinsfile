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
        AWS_CREDENTIALS_ID = 'aws-creds' // reuse for both lambda/ECS
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
