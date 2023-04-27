pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script{
        //             dir('repo') {
        //   git url: 'https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition.git',
        //       branch: 'master',
        //       credentialsId: 'mycredentialsId'
        // }
                    sh 'git clone https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition.git'
                }
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
                    to: 'dimialexiu@gmail.com'
            }
        }
    }
}