pipeline {
    agent any
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
                sh 'sudo docker run -d -p 81:8081 -d rahib0/c27001-assignment'
            }
        }
    }
}