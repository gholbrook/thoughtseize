pipeline {
  agent {
    docker {
      image 'python:3.8.13'
    }

  }
  stages {
    stage('Fetch') {
      steps {
        git(url: 'git@github.com:gholbrook/thoughtseize-ingest.git', poll: true)
      }
    }

    stage('Build') {
      steps {
        sh 'sh "python3 -m pip install -r requirements.txt -y"'
      }
    }

    stage('Test') {
      steps {
        sh 'sh "echo Testing..."'
      }
    }

  }
}