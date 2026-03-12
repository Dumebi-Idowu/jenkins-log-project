pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Dumebi-Idowu/jenkins-log-project'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python log_analyzer.py'
            }
        }

    }
}