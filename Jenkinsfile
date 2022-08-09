pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                sh "make demo-app-build"
            }
        }
        stage('push') {
            steps {
                sh "echo Executing push stage..."
            }
        }
        stage('test') {
            steps {
                sh "echo Executing testing stage..."
            }
        }
        stage('deploy') {
            steps {
                sh "echo Executing deployment stage..."
            }
        }
    }
}