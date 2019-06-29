Got It Onboarding project - Catalog backend using Flask
=======================================================

### Folder structure

    .
    ├── app                         # Main app with all modules
    │   ├── api                     # API calls and routes
    │   │   ├── __init__.py
    │   │   ├── category.py
    │   │   ├── errors.py
    │   │   ├── item.py
    │   │   ├── user.py
    │   ├── models                  # Models for database objects
    │   │   ├── __init__.py
    │   │   ├── category.py
    │   │   ├── errors.py
    │   │   ├── item.py
    │   │   ├── user.py
    │   ├── schemas                 # Schemas for database objects
    │   │   ├── category.py
    │   │   ├── item.py
    │   │   ├── user.py
    │   ├── __init__.py             # Initialize Flask app
    │   ├── authenticate.py         # Authentication helper functions
    │   ├── config.py               # Sets config options
    ├── cfg                         # Config options
    ├── tests                       # Test suites for pytest
    ├── run.py                     
    └── README.md


### Setting up

Create virtual environment
``

Install requirements
`pip install -r requirements.txt`

Create databases (Make sure root user is not password protected)
`mysql -u root`
For development:
`mysql> CREATE DATABASE catalog;`
For testing:
`mysql> CREATE DATABASE test_catalog;`

Set Flask entry point
`export FLASK_APP=run.py`


### Running the app in development

Go to the root folder of the project and type:
`flask run`


### Running test suite

Go to the root folder of the project and type:
`python -m pytest -v tests/`

To see with coverage:
`python -m pytest -v --cov=app tests/`