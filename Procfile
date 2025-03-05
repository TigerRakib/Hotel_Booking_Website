web: gunicorn table_book.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn table_book.wsgi