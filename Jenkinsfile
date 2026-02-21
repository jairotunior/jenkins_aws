pipeline{
    agent any
    triggers {
        githubPush()
    }
    environment{
        AWS_DEFAULT_REGION='us-east-1'
        AWS_ACCESS_KEY_ID = 'test'
        AWS_SECRET_ACCESS_KEY = 'test'
        DOCKER_IMAGE_NAME='jenkins/django-app'
        BUILD_NUMBER='1.0.0'
    }
    stages {
        stage('Unit Test'){
            steps{
                sh ''
            }
        }
        stage('Docker Build'){
            steps{
                //sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ."
                script{
                    docker.build("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}")
                }
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
                sh "${DOCKER_IMAGE_NAME}:latest"
            }
        }
        stage('Deploy'){
            steps{
                sh ''
            }
        }
    }
}