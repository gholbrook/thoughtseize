pipeline {
  agent {
  	docker { image 'python' }
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
