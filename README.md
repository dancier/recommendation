# recommendation

Service that should compute recommendations

## working locally

### first startup locally

`docker-compose up`

terminate with `control-c`

fix permission with:
`sudo chown 5050:5050 -Rvv volumes/pg-admin/`

### normal startup locally

`docker-compose up -d`

### bootstrapping the database locally

(once the services where started locally as seen above)

`python init_db.py`

### using the database ui

(once the services where started locally as seen above)

http://localhost:5050

(see username/password in docker-compose file)

### developing locally

using a virtualenv is strongly recommended:

#### create Virtual Env

`python3 -m venv venv`

(Maybe you have to install _venv_ before with `apt install python3.10-venv`)

#### Activate Venv

`source  ./venv/bin/activate`

#### Install Requirements

`pip install -r requirements.txt`

#### Run the programm

`flask run
`