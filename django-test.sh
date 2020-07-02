python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
coverage erase
coverage run --source='.' --omit=env/* manage.py test
coverage report -m
coverage xml
