# Python Environment

Python3 Path
```which python3```
Create Virtual Environment
```virtualenv -p /usr/bin/python3 my_project```
Activate Environment
```source my_project/bin/activate```
Deactivate
```deactivate```
Delete
```rm -rf my_project```

PIPENV - install
```
pip3 install pipenv
```
Activate - pipfile packages file
```
pipenv shell
```
Freeze - list installed packages
```
pipenv freeze
```
Install
```
pipenv install
```
Install from requirements.txt
```
pipenv install -r ./requirements.txt
```
Check Security Vulnerability
```
pipenv check
```
Exit
```
exit
```
# Django
Create Django Project
```
django-admin startproject testproject
```


https://gist.github.com/jmvsevilleja/d81b456f99e03fb07fb7d9efcb9df441

# python
Python > CPython > Python Bytecode > Python Virtual Machine > Machine Code

LINT = Syntax Error ex. pylint, mypip
PEP8 = Code Formatting ex. x=1 will be x = 1

Built in Functions
https://docs.python.org/3/library/functions.html


>>> dir("") - print available methods in strings

>>> help("".replace) - description

>>> _ = last printed expression
