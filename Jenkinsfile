@Library('jenkins-shared-libraryy') _

pipeline {
  agent any
  stages {
    stage('Lambda Deploy') {
      steps {
        deployLambda(
          functionName: 'myfunction',
          artifactPath: 'build/myfunction.zip',
          awsRegion: 'us-east-1',
          awsCredentialsId: 'aws-creds'
        )
      }
    }
    stage('ECS Deploy') {
      steps {
        deployECS(
          cluster: 'my-ecs-cluster',
          service: 'my-service',
          image: 'repo/app:latest',
          awsRegion: 'us-east-1',
          awsCredentialsId: 'aws-creds'
        )
      }
    }
  }
}
