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
                sh 'ls'
                sh 'touch test.txt'
                echo 'Touching is OK'

            }
        }
    }
}