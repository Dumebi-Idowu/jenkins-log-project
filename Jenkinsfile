pipeline {
    agent {
        docker { 
            image 'python:3.11-slim'
            args '--pull never'
        }
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        APP_VERSION = '1.0.0'
        REPORT_FILE = 'report.txt'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Log Analyzer version ${env.APP_VERSION}"
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Installing pytest...'
                sh 'pip install pytest -q'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python -m pytest test_log_analyzer.py -v'
            }
        }

        stage('Run') {
            steps {
                echo 'Analyzing logs...'
                sh 'python log_analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                echo 'Saving report as artifact...'
                // 👇 This is the artifact magic
                archiveArtifacts artifacts: 'report.txt', 
                                 fingerprint: true,
                                 onlyIfSuccessful: true
            }
        }
    }

    post {
        success { 
            echo '✅ Log analysis complete! Download report.txt from the build page.'
        }
        failure { 
            echo '❌ Pipeline failed. Check the logs.' 
        }
        always { 
            cleanWs() 
        }
    }
}