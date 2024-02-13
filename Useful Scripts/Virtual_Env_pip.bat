@echo off
REM Change directory to your project's directory
cd path\to\your\project

REM Install virtualenv if not already installed
pip install virtualenv

REM Create a virtual environment in the project directory named 'venv'
virtualenv venv

REM Activate the virtual environment
CALL .\venv\Scripts\activate

REM Now you can install any package using pip and it will be installed in your virtual environment
pip install package_name

REM When you're done, you can deactivate the virtual environment
CALL deactivate

REM End of the script
echo Virtual environment is set up and ready to use.
