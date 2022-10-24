pipeline {
    agent any
    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-cred')
	}
    stages {
        stage('Build') {
            steps {
                sh 'sudo docker container prune -f'
                sh 'sudo docker build . -t jacquesguinebault/c270-assignment'
            }
        }

        stage('Run') {
            steps {
                sh 'sudo service docker stop'
                sh 'sudo service docker start'
                sh 'sudo docker run -d -p 81:8081 -d jacquesguinebault/c270-assignment'
            }
        }
    }
}