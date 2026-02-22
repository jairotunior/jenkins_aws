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
        stage('Ruff linting'){
            steps{
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r basic_app/requirements/linting.txt
                # Check for formatting issues that do not break linting rules

                ruff format --check --force-exclude

                # * --select=F,E,W,I                    => Only include rules related to formatting
                # * --force-exclude                     => exclude folders/files configured in `ruff.toml`
                # * --ignore=F403,F405,E722,E721        => Ignore rules that might require additional work
                #
                # Rules ignored:
                # - F403: from {name} import * used; unable to detect undefined names
                # - F405: {name} may be undefined, or defined from star imports
                # - E722: Do not use bare except
                # - E721: Use is and is not for type comparisons, or isinstance() for isinstance checks
                
                ruff check .
                '''
            }
        }
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