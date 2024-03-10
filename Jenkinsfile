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
                bat 'curl -o python-installer.exe https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe' // Download Python installer
                bat 'start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0' // Install Python
            }
        }

        stage('Wait for Python installation') {
            steps {
                // Wait for Python installation to complete
                bat 'timeout /t 120'
            }
        }

        stage('Set up python environment') {
            steps {
                // Check Python version
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
