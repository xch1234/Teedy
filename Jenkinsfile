pipeline {
    agent any
    stages {
        stage('Init') {
            steps {
                script {
                    if (isUnix()) {
                        env.MVN_CMD = 'mvn'
                    } else {
                        env.MVN_CMD = 'mvn'
                    }
                }
            }
        }
        stage('Clean') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} clean"
                    } else {
                        bat "${env.MVN_CMD} clean"
                    }
                }
            }
        }
        stage('Compile') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} compile"
                    } else {
                        bat "${env.MVN_CMD} compile"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} test -Dmaven.test.failure.ignore=true"
                    } else {
                        bat "${env.MVN_CMD} test -Dmaven.test.failure.ignore=true"
                    }
                }
            }
        }
        stage('PMD') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} pmd:pmd"
                    } else {
                        bat "${env.MVN_CMD} pmd:pmd"
                    }
                }
            }
        }
        stage('JaCoCo') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} jacoco:report"
                    } else {
                        bat "${env.MVN_CMD} jacoco:report"
                    }
                }
            }
        }
        stage('Javadoc') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} javadoc:javadoc"
                    } else {
                        bat "${env.MVN_CMD} javadoc:javadoc"
                    }
                }
            }
        }
        stage('Site') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} site"
                    } else {
                        bat "${env.MVN_CMD} site"
                    }
                }
            }
        }
        stage('Package') {
            steps {
                script {
                    if (isUnix()) {
                        sh "${env.MVN_CMD} package -DskipTests"
                    } else {
                        bat "${env.MVN_CMD} package -DskipTests"
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/site/**/*.*', fingerprint: true
            archiveArtifacts artifacts: '**/target/**/*.jar', fingerprint: true
            archiveArtifacts artifacts: '**/target/**/*.war', fingerprint: true
            junit '**/target/surefire-reports/*.xml'
        }
    }
}