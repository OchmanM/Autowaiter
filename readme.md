# Order Management

## About this application

## Install
- To change Database go to "RM/settings.py" and find "DATABASE = " then change database (visit here for more https://docs.djangoproject.com/en/1.10/ref/settings/#databases). Default Database is MySql.

- Migrate Database by typing this:
```
python manage.py migrate
```
## Login Credentials
- To add admin user, use
```
py manage.py createsuperuser
```

## Features
- Add order
- Add products
- Export Order (pdf, excel, csv and etc)
- Edit / Delete Order
- Search Order
- Print

## Uses
* Restaurants, bars etc
