pipeline {
agent any
    parameters {
            choice(
                name: 'TESTS',
                choices:"All\nHWMS tests\nMensa Functional\nMensa Integration",
                description: "Which tests to run ")
            choice(
                name: 'ENVIRONMENT',
                choices:"eu_prod\nus_prod",
                description: "Environment of the tests" )
            string(
                name: 'TESTRAIL_RUN_NAME',
                defaultValue:"JenkinTestRun",
                description: "Test rail testrun name")
            booleanParam(
                name: 'SKIP_BUILD',
                defaultValue: false,
                description: 'Skips build pipenv setup')
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
                bat 'python -m pipenv run pytest scripts -v --env=${ENVIRONMENT} --junitxml=result.xml --testrail --tr-config=testrail.cfg --tr-testrun-name=${TESTRAIL_RUN_NAME}'
                break
            case "HWMS tests":
                bat 'python -m pipenv run pytest scripts -m hwms_functional -v --env=${ENVIRONMENT} --junitxml=result.xml --testrail --tr-config=testrail.cfg --tr-testrun-name=${TESTRAIL_RUN_NAME}'
                break
            case "Mensa Functional":
                bat 'python -m pipenv run pytest scripts -m mensa_functional -v --env=${ENVIRONMENT} --junitxml=result.xml --testrail --tr-config=testrail.cfg --tr-testrun-name=${TESTRAIL_RUN_NAME}'
                break
            case "Mensa Integration":
                bat 'python -m pipenv run pytest scripts -m mensa_integration -v --env=${ENVIRONMENT} --junitxml=result.xml --testrail --tr-config=testrail.cfg --tr-testrun-name=${TESTRAIL_RUN_NAME}'
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
