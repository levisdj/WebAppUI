# Introduction 
This is the "Successful Login Automation" small project of the Smood WebApp; this is done as part of the hiring process.
The project as been done Using Selenium coupled with Python and following the Page Object Model framework/structure. 

# Getting Started

# Project folders strucrue:
WebAppUITestProject\
→	drivers ==> all drivers are located here\
→	pageObjects ==> should hold a single python class (containing page Locators and page Actions) for each page\
→	reports\
→	screenshots ==> In case of failures a screenshot is saved in this folder\
→	testCases\
→→		chrome\
→→		firefox\
→→		safari\
→→		variables.py ==> Hold all variables used in the automation project\
→	testSuites ==> used to create specific testSuites like SanityTest\
→	utility ==> all utilities functions/objects shared go here \
→	venv ==> The virtual environment folder, it holds python version for the Project, script to activate and deactivate the environment\
→	README.md\
→	requirement.txt\
→	run.bat

# 1. Installation process
	- Operating System: The project has been done on Windows 10;	
	- Copy the project to C:\;
	- Add the project directory to Windows environment variables;

# 2. Software dependencies
	- Selenium release version: selenium~=3.141.0;
	- Python interpreter 3.9.* or latest;
	- Chrome version: Version 92.0.4515.159;
	- chromedriver version: ChromeDriver 92.0.4515.107;
	- Firefox version: 91.0 (64 bits);
	- geckodriver version: geckodriver-v0.29.1-win64;
	- Safari is not supported;
	
# 3 How to Run the Tests?
	You have at your disposal 3 different options to run the tests and generate the report.
# 3.1 First option - "run.bat" file:
	assumption: the python interpreter is already installed in the operating system;
	1. double on the the "run.bat" from the project root (this will open a command prompt with the python virtual envionement activated);
	2. enter the following command "run.bat" and press ENTER from the keyboard;
	3. all the tests (in the directory testCases) will run (opening physically the browser) and a Report will be generated in the 'reports' directoty;

# 3.2 Second option - from PyCharm running the whole testCases folder:
	1. donwload pycharm community version
	2. import the project directory (File\Open\<select the project directoru>);
	3. select the Python Interpreter location from pycharm in (File\Settings\<Project name>\Python interpreter\);
	4. Right on the testCases folder and select the option "Run Unittest in testCases";
	5. Once finished the report in the 'reports' folder will be updated (overriding);

# 3.3 Third option - from PyCharm running the testSuites module:
	 Once you have indicated to pycharm the location of the python interpreter right-click and run the module "testRunsWebAppUI.py" from testSuites folder;

# 4. Download links:
	If you want to download pycharm community you can go here: https://www.jetbrains.com/pycharm/download/#section=windows;
	If you want to download the python interpreter you can go here: https://www.python.org/downloads/;
