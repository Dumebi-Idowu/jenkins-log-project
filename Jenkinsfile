pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }

    stages {

        stage('Checkout Repo') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install --upgrade pip -q'
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Running log analyzer...'
                sh 'python log_analyzer.py'
            }
        }
    }

    post {
        success { 
            echo 'Pipeline completed successfully! ✅' 
        }
        failure { 
            echo 'Pipeline failed. Check the logs. ❌' 
        }
        always {
            cleanWs()
        }
    }
}