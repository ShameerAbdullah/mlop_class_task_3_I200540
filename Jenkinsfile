pipeline {
    agent {
        label 'ubuntu-latest'
    }

    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: ubuntu-latest'
            }
        }

        stage('Download and install Python') {
            steps {
                sh 'curl -o python-installer https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe' // Download Python installer
                sh 'python-installer /quiet InstallAllUsers=1 PrependPath=1 Include_test=0' // Install Python
            }
        }

        stage('Set up python environment') {
            steps {
                sh 'python --version'
            }
        }

        stage('Installing dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Executing test cases') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
