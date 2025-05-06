# Lite API

Simple litestar CRUD operations with users

Clone repo:
```
git clone https://github.com/rust3r/liteapi.git
```

## Run in docker
```
docker-compose up -d
```

## Run from source

Install dependencies
```
poetry install --no-root
```

Create new database in postgres:
```
CREATE DATABASE liteapi;
```

Run server
```
poetry run litestar run --reload
```