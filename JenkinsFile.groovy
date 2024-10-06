pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_calculator.py'
            }
        }
        stage('Lint Code') {
            steps {
                sh 'flake8 app.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'flask run --host=0.0.0.0'
            }
        }
    }
}
