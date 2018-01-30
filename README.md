# Django Website Starter
Starting template for Django 2 powered websites.

## Requirements
- Python 3.5+
- Django 2+
- dj-database-url
- whitenoise
- python-decouple
- gunicorn	
- psycopg2

## Features
- config variables with python-decouple
- database config with dj-database-url
- static files serving with Whitenoise
- default email backend config
- example homepage template using Bootstrap 4
- ready for Heroku deployment

## Config Variables
Create `.env` file in `src` directory and specify config variables, e.g.:
```
SECRET_KEY=2fi-6jj!0pr_02%1@wr1f295vq#1mji#z8gyx875d%gq(z6(1u
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite://///home/m/code/django-website-starter/src/db.sqlite3
```
