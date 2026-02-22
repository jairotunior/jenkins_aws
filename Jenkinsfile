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
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r basic_app/requirements/requirements.txt
                chmod +x basic_app/run_unit_test.sh
                cd basic_app && ./run_unit_test.sh
                '''
            }
        }
        stage('Docker Build'){
            steps{
                script{
                    dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
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