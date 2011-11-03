#!/bin/bash

# abort on any errors
set -e

# create the virtual environment, install/update required packages
virtualenv --no-site-packages ../polipop-virtualenv
source ../polipop-virtualenv/bin/activate
pip install -r requirements.txt

# make sure that there is no old code (the .py files may have been git deleted) 
find . -name '*.pyc' -delete

# Compile the CSS
sass --scss --update --style compressed .

# go to the project directory for local config
cd ./polipop

# get the database up to speed
./manage.py syncdb
./manage.py migrate

# gather all the static files in one place
./manage.py collectstatic --noinput

cd --
