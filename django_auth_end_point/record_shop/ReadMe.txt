SETUP FOR FIRST TIME

In here (in record_shop) setup a python environment and login to it
python3 -m venv .env

source .env/bin/activate

Make sure Django is installed
pip3 install django


From the environment go into record_store and do some setup with the database
cd record_store


python3 manage.py flush
python3 manage.py migrate
python3 manage.py createsuperuser


IF EVERYTHING IS RUNNING FINE YOU JUST NEED TO DO THIS IN record_store

python3 manage.py runserver


You can find the admin menu here
http://127.0.0.1:8000/admin/

and the main page is here
http://127.0.0.1:8000/inventory/