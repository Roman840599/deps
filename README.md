# deps

Application already contains alembic migration system, logging with loguru, tests with pytests.

To start exploatation user need to put DB credentials in envs(.env.dev.db file intended for db credentials in web containes, .env.dev.db.docker for credentials in db container).
From .env.dev.db DB creds will be passed to configs/db_config.py, where alredy realized Pydantic DBSettings class. This class is responsible for credentials validation and creation sqlalchemy_url. Alembic and database engine will get sqlalchemy_url from DBSettings class.

Migrations alredy created and located in alembic/versions/. When command 'docker-compose up' will be fulfilled, docker-compose at first will perform command 'alembic upgrade head' to perform migrations and then will run an application.

