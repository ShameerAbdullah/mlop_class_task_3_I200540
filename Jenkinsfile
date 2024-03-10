pipeline {
    agent {
        label 'ubuntu-latest' // Specify the label for the Ubuntu agent
    }
    stages {
        stage('Setting of runner') {
            steps {
                echo 'runs-on: ubuntu-latest' // Echo the OS to confirm
            }
        }

        stage('Download and install Python') {
            steps {
                sh 'sudo apt update' // Update package lists
                sh 'sudo apt install -y python3 python3-pip' // Install Python and pip
                sh 'python3 --version' // Check Python version
            }
        }

        stage('Set up python environment') {
            steps {
                sh 'python3 --version' // Check Python version again
            }
        }

        stage('Installing dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt' // Install Python dependencies
            }
        }

        stage('Executing test cases') {
            steps {
                sh 'python3 main.py' // Execute main.py
            }
        }
    }
}
