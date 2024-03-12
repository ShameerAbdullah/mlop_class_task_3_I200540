pipeline {
    agent {
        label 'ubuntu-latest'
    }
    stages {
        stage('Set up Python environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
        stage('Installing dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Executing test cases') {
            steps {
                sh 'pytest test.py'
            }
        }
    }
}
