pipeline{
    agent any
    triggers {
        githubPush()
    }
    environment{
        AWS_DEFAULT_REGION='us-east-1'
        AWS_ACCESS_KEY_ID = 'test'
        AWS_SECRET_ACCESS_KEY = 'test'
        AWS_CREDENTIALS = credentials('aws-credentials')
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
        stage('Docker Build and Push'){
            steps{
                script{
                    def app = docker.build("${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}", "-f basic_app/docker/server/Dockerfile basic_app")
                    // Push and other docker steps run on the same agent (same Docker daemon)
                    // sh 'docker login -u ${}'
                    // docker.image("${env.DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}").push('latest')
                }
            }
        }
        stage('Push Image to AWS'){
            steps{
                script{
                    docker.withRegistry(
                        "http://000000000000.dkr.ecr.us-east-1.localhost.localstack.cloud:4566/ecr-repository",
                        "ecr:${AWS_DEFAULT_REGION}:aws-credentials"
                    ){
                        // def app = docker.image("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}")
                        app.push("${BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
    }
}