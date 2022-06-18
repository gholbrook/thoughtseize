pipeline {

  agent {
  	docker {
  		image "python:3.8.13"
  		reuseNode true
  	}
  }

  stages {
  	stage("Fetch") {
  		steps {
  			git branch: "main", url: "git@github.com:gholbrook/thoughtseize.git"
  		}
  	}
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
