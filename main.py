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

import requests #import module


user = {"name": { "title": "Mr", "first": "John", "last": "Smith"}}
title = None
firstName = None
lastName = None


if user is None:
    response = requests.get('https://randomuser.me/api')
    data = response.json()
    user = data['results'][0]


#5. assign the randomn name
title = user["name"]["title"]
firstName = user["name"]["first"]
lastName = user["name"]["last"]
greeting = f'Hello {title} {firstName} {lastName}'


#6. print greeting based on the fetch data
functionOnPython(greeting) # will print random first name


#7. working with JSON data 
import json

jsonData = json.loads('[{"id": 1, "species": "dog"}]')
print(jsonData[0])


