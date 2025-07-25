## Django REST API Demo System API

## How to run code command line


git clone https://github.com/Suhas-Shende/system-api


cd system-api

sysenv/scripts/activate

cd demoproject
```python
# Before running python manage.py makemigrations and python manage.py migrate
#Make Sure You have Mysql Workbench
#Please in settings.py of demoproject folder set my mysql database connection

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',     # MySQL backend
        'NAME': 'sys_db',                         #create database sys_db
        'USER': 'Your_User_Name',                 #Datbase USER name
        'PASSWORD': 'Type_Your_Password',         #Your USER Password
        'HOST': 'localhost',                      # Or IP address
        'PORT': '3306',                           # Default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


```

python manage.py makemigrations 

python manage.py makemigrations demoapp 

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

