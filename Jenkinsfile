pipeline {
  agent {
    docker {
      image 'python'
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