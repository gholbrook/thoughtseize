pipeline {
  agent {
  	docker { image 'python:3.8.13' }
  }

  environment {
 	PRODUCT = 'ghcli'
    GIT_HOST = 'somewhere'
    GIT_REPO = 'repo'
  }

  stages {
  	stage("Build") {
  		steps {
  			sh "python3 -m pip install -r requirements.txt -y"
  		}
  	}
  	stage("Test") {
  		steps {
  			sh "echo Testing..."
  		}
  	}
  }
}
