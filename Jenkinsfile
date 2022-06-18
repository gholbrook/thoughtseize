pipeline {
  agent any
  stages {
  	stage("Fetch code") {
  		steps {
  			git branch: "main", url: "git@github.com:gholbrook/thoughtseize.git"
  		}
  	}
  	stage("Build") {
  		steps {
  			sh "apt-get update"
  			sh "apt-get install python3.8"
  			sh "python3 -m pip install -r requirements.txt"
  		}
  	}
  	stage("Test") {
  		steps {
  			sh "echo Testing..."
  		}
  	}
  }
}
