import requests #import module

"""
FOR WINDOWS

Hello. In this file you will find the basic functions on python and how to use it.
1. make sure you have installed python in your machine (recommended 3.7.7).
2. create a folder.
3. create a virtual env (venv) -> in powershell call: `py -m venv {name of the virtual env}`.
4. activate the virtual env -> in powershell call: {name of venv}\Scripts\activate.bat.
5. create a python file and start coding

Tips: 
 - use triple " for multiline comments, like this segment for example 
 - use # for single line comments

"""


#1. print statement 
print('==== start python ==== ')

#2. define a function 
def functionOnPython(message):
    """Simple function to illustrate the use of python 
        generated using Python Docstring Generator
    Arguments:
        message {String} -- Message that you want to print

    Returns:
        String -- Message to be printed
    """    
    message = message
    return print(message)

#3. calling the function
functionOnPython('this is my message')

#4. assigning variable when using requests module 
# recommended extension to use with this AREPL 

user = None
title = None
firstName = None
lastName = None
fullName = None


if user is None:
    response = requests.get('https://randomuser.me/api')
    data = response.json()
    user = data['results'][0]
else:
    #5. assign the randomn name
    title = user["name"]["title"]
    firstName = user["name"]["first"]
    lastName = user["name"]["last"]
    fullName = f'Hello {title} {firstName} {lastName}'

if fullName is not None:
    functionOnPython(fullName) # will print random first name





