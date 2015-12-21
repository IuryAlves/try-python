# Try Python [![Build Status](https://travis-ci.org/IuryAlves/TryPython.svg?branch=master)](https://travis-ci.org/IuryAlves/TryPython)

## Try python is a project inspired by [try-haskell](tryhaskell.org)


![try-python](try-python.gif)
##### The goal of this project is to introduce python for new people by let they use a python REPL( Read, Eval, Print, Loop) in the browser.

## Getting Started

* Install python 2.x on your system
*  Install git
* Clone this repository
 
        git clone git@github.com:IuryAlves/TryPython.git
        cd TryPython

* Install python virtualenv: 
 
        sudo pip install virtualenv

* Create a virtualenv:
 
        virtualenv venv
        source venv/bin/activate

* Install project dependencies:

        pip install -r requirements.txt

* Sync the database

        ./manage.py syncdb

* Run
        
        export DJANGO_SECRET_KEY=<your-secret-key> 
        cd TryPython
        ./manage.py runserver 8000


Now, just access localhost:8000 =D

## Contributing

 * Install nodejs
 
 
        npm install  # on project root path

* Run js tests and lint


        npm test
    
This project uses TravisCI [TryPython on Travis](https://travis-ci.org/IuryAlves/TryPython)


There are a lot of things to do.

* You can check the issues of the project to know in what you can contribute
* You can access the wiki to know how run this using pypy in a sandbox and also discover how the security against malicious users are implemented.

This project uses [jquery.console](https://github.com/chrisdone/jquery-console)
