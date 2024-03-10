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
                script {
                    def pythonInstaller = 'python-installer.exe'
                    def pythonInstallerUrl = 'https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe'
                    
                    // Download Python installer
                    bat "curl -o ${pythonInstaller} ${pythonInstallerUrl}"
                    
                    // Install Python
                    bat "start ${pythonInstaller} /quiet InstallAllUsers=1 PrependPath=1 Include_test=0"
                    
                    // Wait for Python installation to complete
                    timeout(time: 15, unit: 'MINUTES') {
                        def installerProcess = "tasklist /FI \"IMAGENAME eq ${pythonInstaller}\" | findstr ${pythonInstaller}".execute()
                        def installerExitCode = installerProcess.waitFor()

                        if (installerExitCode == 0) {
                            echo "Python installation is still in progress. Waiting..."
                            sleep(30) // Adjust the sleep duration based on installation time
                        }
                    }
                }
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
