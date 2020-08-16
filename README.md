HTTP_200
=============


[![Build Status](https://travis-ci.org/ncs-jss/HTTP_200.svg?branch=master)](https://travis-ci.org/ncs-jss/HTTP_200)
[![Coverage Status](https://coveralls.io/repos/github/ncs-jss/HTTP_200/badge.svg?branch=master)](https://coveralls.io/github/ncs-jss/HTTP_200?branch=master)


A new Information Center for JSS Academy of Technical Education, Noida. 

# Installation

The production HTTP_200 server is running on Ubuntu, so this is
probably the easiest environment in which to get things running, but other
distributions of linux should be fine as well. We use Apache on the
production server, but HTTP_200 will run standalone for testing as well.

### Virtual environment (if your system doesn't have it already):

The development environment relies on using a Python [virtual environment][venv]
for tools and portability across platforms. Ensure that you have Python Pip
installed for your platform before proceeding with these instructions.

Windows users can use the [following guide][windows venv]. Specifically, get
Python installed and then use the get-pip.py installer once Python is working

OSX users can use the built in version of Python as long as Pip is available,
or better, install [Brew and Python][osx venv].

Linux users should have Python already installed. Ensure Pip is installed via
your package manager and you should be all set.

## Instructions to get started with HTTP_200 development

HTTP_200 is built very cleanly. For setting the development environment on your machine, you need to follow the steps described in the next section. 

## Linux based Setup for HTTP_200 development

Note: Ubuntu 14.04 LTS is recommended to use for the development environment.

1. Run the following git clone (specify a directory of your choosing if you like):

        git clone https://github.com/ncs-jss/HTTP_200.git http_200

2. Run virtualenv on the git cloned directory to setup the Python virtual environment:

        virtualenv http_200

3. cd into the name of the directory into which you cloned the git repository

        cd http_200

4. Activate the virtual environment:

        source bin/activate

5. After activating the virtual environment, install the dependencies

        pip install -r requirements/common.txt
        pip install -r requirements/dev.txt (For development)

6. Now, create the database migrations so as to use the Database

        python manage.py syncdb

7. For creating groups, run the following command 

	    python manage.py createdata
        
8. (Optional) For creating random faculties, students and notices

        python manage.py createdata --dummydata

	this will create:
	1. faculty_admin: username = admin, password = admin
	2. student_admin: username = student, password = student
	3. 20 other faculties' and students' accounts with password = default

8. You are all set. Run the final command

        python manage.py runserver

10. Its time to rock. Visit [http://localhost:8000][localhost] in your browser and you should be all set.


[venv]: http://pypi.python.org/pypi/virtualenv
[wrapper]: http://www.doughellmann.com/projects/virtualenvwrapper/
[windows venv]: http://docs.python-guide.org/en/latest/starting/install/win/
[osx venv]: http://docs.python-guide.org/en/latest/starting/install/osx/
[bug]: https://github.com/docker/docker/issues/9628
[localhost]: http://localhost:8000/

