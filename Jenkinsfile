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
                sh 'command -v docker >/dev/null 2>&1 || { echo "ERROR: Docker is not installed or not in PATH on this agent. Install Docker on the agent or run this stage on a node with Docker."; exit 1; }'
                sh "docker build -t ${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} -f basic_app/docker/server/Dockerfile basic_app"
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