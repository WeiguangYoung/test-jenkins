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
                sh 'pwd'
                sh 'cd /tmp'
                sh 'pwd'
                sh 'touch test.txt'
                echo 'Touching is OK'

            }
        }
    }
}