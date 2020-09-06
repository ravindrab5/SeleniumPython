FOR /F "tokens=4 delims= " %%i in ('route print ^| find " 0.0.0.0"') do set localIp=%%i
java -jar selenium-server-standalone-3.11.0.jar -role webdriver -hub http://%localIp%:4444/grid/register -nodeConfig node.json
::-Dwebdriver.chrome.driver="./chromedriver.exe"