# SQLAlchemy Base Setup

This project demonstrates a minimal working foundation for SQLAlchemy. There are no schemas/models included, but the [`core/database`](./src/sqlalchemy_setup/core/database/) directory contains all of the data needed to set up a Postgres or SQLite database for the project.

Settings are loaded from the environment and defined as importable variables in [`constants.py`](./src/sqlalchemy_setup/constants.py).

Dependencies like the script/app's SQLAlchemy `engine` and `session` are defined in [`dependencies.py`](./src/sqlalchemy_setup/dependencies.py), and can be imported throughout the app.
