pipeline {
    agent any

    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: windows-latest' // Assuming you are running Jenkins on a Windows agent
            }
        }

        stage('Set up python environment') {
            steps {
                bat 'python --version' // Using 'python' instead of 'python3' for Windows
            }
        }

        stage('Installing dependencies') {
            steps {
                bat 'pip install -r requirements.txt' // Using 'pip' instead of 'pip3' for Windows
            }
        }

        stage('Executing test cases') {
            steps {
                bat 'python main.py' // Assuming 'main.py' is the main script to execute
            }
        }
    }
}
