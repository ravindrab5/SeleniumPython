pipeline {
agent any
    parameters {
            choice(
                name: 'TESTS',
                choices:"All\nHWMS tests\nMensa Functional\nMensa Integration",
                description: "Which tests to run ")
            choice(
                name: 'ENVIRONMENT',
                choices:"qa01\nqa02",
                description: "Environment of the tests" )

    }
   stages {
	stage('Clone'){
		steps{
		git branch: 'master',
    			     credentialsId: '8fcd4d42-45f9-4d27-8f24-b5364e0268d9',
                             url: 'https://github.com/ravindrab5/SeleniumPython.git'
		}
         }

   stage('Build'){
			steps{
			script{
			if (!params.SKIP_BUILD){
                bat 'python -m pip install pipenv'
                bat 'python -m pipenv install --ignore-pipfile'
			}
			}
			}
  }
stage('Run Tests'){
			steps{
			script{
			switch(TESTS){

            case "All":
                bat python -m pipenv run pytest scripts -v --en=params.ENVIRONMENT --junitxml=result.xml
                break
            }
            }
        	}
  }

}
post {
  always {
    junit "**/result.xml"
  }
}
}
