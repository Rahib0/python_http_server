pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'sudo docker container prune -f'
                sh 'sudo docker build . -t rahib0/c27001-assignment'
            }
        }

        stage('Run') {
            steps {
                sh 'sudo service docker stop'
                sh 'sudo service docker start'
                sh 'sudo docker run -d -p 81:8000 -d rahib0/c27001-assignment'
            }
        }

        stage('Push to Dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'sudo docker push rahib0/c27001-assignment'
            }
        }
        post {
            always {
                sh 'sudo docker logout'
            }
        }
    }
}