pipeline {
    agent any
        stages {
          stage('Git clone and environment setup') {
            steps{
              script {
                 git branch: "main", credentialsId: '49cba28e-f273-4f02-b3e5-ba35566f200c', url: 'https://github.com/DineshSurpur/gitproject.git'
              }
            }
          }
          stage('Execute python script') {
            steps{
              script {
                sh '/usr/local/bin/python3 py-files/hello.py'
              }
            }
          }
        }
}
