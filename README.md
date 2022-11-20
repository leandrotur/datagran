# Python-Flask-MongoDB-Celery-redis-with-Docker-Compose
Launching Tech Stack in order to Python, Flask Framework and MongoDB with Docker Compose. 



## Execution this Docker Compose.

First, making clone to this project, doing: 

```bash
git clone https://github.com/leandrotur/datagran.git
```

And then, execute the Docker Compose instruction to launch Tech Stack (`Python(web)`, `Celery(worker)`, `redis`, `mongoDB_express` and `MongoDB(database)`). 

```bash
docker-compose up -d
```

## Modify credentials for MongoDB Server

Update the file `.env` (environment variables) with your specify credentials. 

```bash
WEB_HOST=datagran_api

MONGO_HOST=datagran_db
MONGO_PORT=27017
MONGO_USER=root-datagran
MONGO_PASS=password-datagran
MONGO_DB=local
```

Other important file is `mongo-init.js`.

```javascript
db.createUser(
    {
        user: 'root-datagran',
        pwd: 'password-datagran',
        roles: [
            { role: "clusterMonitor", db: "admin" },
            { role: "dbOwner", db: "local" },
            { role: 'readWrite', db: 'local' }
        ]
    }
)
```



## Testing MongoDB Connection as an API


$ use postman: http://127.0.0.1:8000/new_task ( with this body {"cmd": "ls"} )
use postman: http://127.0.0.1:8000/get_output?id={ID} 

Examples of get_output and new_task end points: https://www.getpostman.com/collections/d1f33f61f8d6efea55d5

```

## Other instructions

#### Remove volumes
We have two ways to remove our volumes with Docker.

First is using `prune` command.

```bash
docker volume prune -f
```

Second is using the current command `volume rm` with `-f` like parameter.

```bash
docker volume rm $(docker volume ls -q)
```

#### Clean up MongoDB volume and Cache for Python

```bash
rm -rf mongo-volume app/__pycache__/ && mkdir mongo-volume
```

#### Delete cache in Docker System

```bash
docker system prune -a -f && docker builder prune -a -f
```

### Recreate container web

```bash
docker-compose up --build --force-recreate --no-deps -d web
```

### Show logs of API Execution

```bash
docker logs --tail 1000 -f datagran_api
```
