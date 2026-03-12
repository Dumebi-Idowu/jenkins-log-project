pipeline {
    agent any

    stages {

        stage('Checkout Repo') {
            steps {
                // Checkout the main branch from your repo
                checkout([$class: 'GitSCM', 
                    branches: [[name: 'main']], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/Dumebi-Idowu/jenkins-log-project.git',
                        credentialsId: 'github' // optional, only if private
                    ]]
                ])
            }
        }

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 log_analyzer.py
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}