
  virtualenv env
  source env/bin/activate
  python setup.py develop
  cd example
  pip install -r requirements.txt
  python manage.py syncdb
  python manage.py runserver
