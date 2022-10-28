from flask.cli import FlaskGroup
from app import app

# https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#gunicorn

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()

