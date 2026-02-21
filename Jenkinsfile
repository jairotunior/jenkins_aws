pipeline{
    agent any
    environment{
        AWS_DEFAULT_REGION='us-east-1'
        AWS_CREDENTIALS=credentials('aws-credentials')
    }
    stages {
        stage('Unit Test'){
            steps{
                sh ''
            }
        }
        stage('Docker Build'){
            steps{
                sh 'docker build -t jenkins/django-app:latest .'
            }
        }
        stage('Integration Test'){
            steps{
                sh 'run_integration_test.sh'
            }
        }
        stage('Push Images'){
            steps{
                sh 'docker login -u ${}'
                sh 'docker push jenkins/django-app:latest'
            }
        }
        stage('Deploy'){
            steps{
                sh ''
            }
        }
    }
}