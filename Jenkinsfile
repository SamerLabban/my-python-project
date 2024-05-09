pipeline {
    agent any

    stages {
        stage('Docker Compose Build and Run') {
            steps {
                // Builds the Docker image and runs the container detached
                script {
                    sh 'docker-compose up --build -d'
                }
            }
        }
        stage('Test') {
            steps {
                // Executes pytest within the Docker environment
                script {
                    sh 'docker-compose run --rm calculator-app python -m pytest'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Bring down the containers, removing containers, networks, and images
            sh 'docker-compose down --rmi local'
        }
        success {
            echo 'Build was successful and tests passed.'
        }
        failure {
            echo 'Build failed or tests did not pass.'
        }
    }
}
