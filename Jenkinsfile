pipeline {
    agent any

    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: windows-latest'
            }
        }

        stage('Installing dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Executing test cases') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
