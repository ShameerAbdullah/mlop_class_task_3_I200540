pipeline {
    agent any

    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: ubuntu-latest'
            }
        }

        stage('Set up python environment') {
            steps {
                sh 'python3 --version'
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
