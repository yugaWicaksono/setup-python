#Base commands in Windows 

This document summarize all of the base commands for setting up python in windows 

## Environment 

### Virtual env  
`py -m venv venv` this will generate virtual env with the name venv

### Activate the environment 

Make sure that your current directory contains the `venv` folder (or however you called it)
In powershell call `.\venv\Scripts\activate.ps1`


## Modules

### Install

when pip is installed you can use this command to install module:

* `py -m pip install requests` will install requests module

### Uninstall

to uninstall follow the following steps 

1. `pip freeze > requirements.txt`
2. `pip uninstall -r requirements.txt` to remove one by one 
3. `pip uninstall -y -r <(pip freeze)` to remove all without overwriting requirement.txt

from: https://stackoverflow.com/questions/11248073/what-is-the-easiest-way-to-remove-all-packages-installed-by-pip

## Issues with activation of venv

If you have error when activating eyour virtual env, you can check the following links to fix it


https://github.com/Microsoft/vscode-python/issues/2559#issuecomment-441815078

https://docs.microsoft.com/da-dk/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1
