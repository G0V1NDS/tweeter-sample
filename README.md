## Project Setup

### Requirements

### System requirements:
* `Python 3.6+`

### Getting started

#### Create virtual environment
`python3 -m venv env`

#### Activate the environment
`source env/bin/activate`

```cd <project_root>```

##### Create `.env` file
###### ***`Copy env variables from .sample.env file and insert in the .env file.`

#### Export the env variables
```
export DB_HOST="0.0.0.0"
export DB_NAME=<db-name>
export DB_USERNAME=<db-username>
export DB_PASSWORD=<db-password>
export DJANGO_SETTINGS_MODULE="main.settings.development"
export DB_PORT=<db-port>
```

#### Migrations
`python manage.py migrate`

#### Run the project
`python manage.py runserver 0.0.0.0:8000`
