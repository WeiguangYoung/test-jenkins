pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                sh 'cd /tmp'
                sh 'touch test.txt'
                echo 'Touching is OK'

            }
        }
    }
}