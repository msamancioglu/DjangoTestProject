# DjangoTestProject
Testing a project written in Django + Rest Frameworks


## create and activate virtual env

python3 -m venv env

. env/bin/activate


## install project requirements
pip3 install -r requirements.txt

# Run django test and create coverage xml/report

## delete old reports(if any)
coverage erase

## run django test(manage.py test) and create test coverage 
coverage run --source='.' --omit=env/* manage.py test

## show coverage report
coverage report

## create coverage.xml
coverage xml
