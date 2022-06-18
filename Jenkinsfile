pipeline {
  agent any
  stages {
  	stage('Fetch code') {
  		steps {
  			git branch: 'main', url: 'git@github.com:gholbrook/thoughtseize.git'
  		}
  	}
  	stage('Build') {
  		steps {
  			sh 'echo Building...'
  			sh 'python -m pip install -r requirements.txt'
  		}
  	}
  	stage('Test') {
  		steps {
  			sh 'echo Testing...'
  		}
  	}
  }
}
