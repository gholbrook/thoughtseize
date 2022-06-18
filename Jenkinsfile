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
  			sh "apt-get install sudo -y"
  			sh "sudo apt-get update -y"
  			sh "sudo apt-get install python3.8 -y"
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
