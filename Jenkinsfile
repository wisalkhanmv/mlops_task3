pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 test_test.py'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'deployed'
            }
        }
    }
}