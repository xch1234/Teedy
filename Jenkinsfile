pipeline {
    agent any

    tools {
        maven 'M3'
    }

    environment {
        // Docker Hub credentials ID stored in Jenkins
        DOCKER_HUB_CREDENTIALS = 'dockerhub_credentials'
        // Docker Hub repository: <username>/<repo>
        DOCKER_IMAGE = 'emilyxiang/emily_teedy'
        // Use Jenkins build number as image tag
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Build') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/master']],
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/EmilyXiang0/Teedy.git']]
                )
                bat 'mvn -B -DskipTests clean package'
            }
        }

        stage('Building image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}")
                }
            }
        }

        stage('Upload image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
                        docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").push()
                        docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").push('latest')
                    }
                }
            }
        }

        stage('Run containers') {
            steps {
                script {
                    bat 'docker stop teedy-container-8082 || exit 0'
                    bat 'docker rm   teedy-container-8082 || exit 0'
                    bat 'docker stop teedy-container-8083 || exit 0'
                    bat 'docker rm   teedy-container-8083 || exit 0'
                    bat 'docker stop teedy-container-8084 || exit 0'
                    bat 'docker rm   teedy-container-8084 || exit 0'

                    docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").run(
                        '--name teedy-container-8082 -d -p 8082:8080'
                    )
                    docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").run(
                        '--name teedy-container-8083 -d -p 8083:8080'
                    )
                    docker.image("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}").run(
                        '--name teedy-container-8084 -d -p 8084:8080'
                    )

                    bat 'docker ps --filter "name=teedy-container"'
                }
            }
        }
    }
}
