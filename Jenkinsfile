pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition'
            }
        }
        stage('List files') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Send email') {
            steps {
                emailext body: 'Click on the following link to view the build: ${BUILD_URL}',
                    subject: 'Build ${BUILD_NUMBER} finished',
                    to: 'jussi.pollari@msd.com'
            }
        }
    }
}
