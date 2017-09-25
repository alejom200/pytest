#!/usr/bin/env groovy

timestamps {
  properties([parameters([choice(choices: 'pb-devops01-edge-dbp\npb-devops02-edge-dbp\narbp01\nOSImageBuildHost', description: 'Node on which to build this project.', name: 'JENKINS_NODE')]) ])

  node("${JENKINS_NODE}") {
    stage('Checkout relevant GIT repos') {
      checkout scm
    }
    stage('Copy SSH key to each VM') {
      sh './test.sh'
    }
  }
}
