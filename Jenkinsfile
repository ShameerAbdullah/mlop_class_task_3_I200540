pipeline {
    agent any

    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: windows-latest'
            }
        }

        stage('Download and install Python') {
            steps {
                bat 'curl -o python-installer https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe' // Download Python installer
                bat 'python-installer /quiet InstallAllUsers=1 PrependPath=1 Include_test=0' // Install Python
            }
        }

        stage('Set up python environment') {
            steps {
                bat 'python --version'
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
