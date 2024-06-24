# Open Vault

A file hosting service that you can quickly deploy on your server.

## Configuring

Create `.env` file for web application:

```
SECRET_KEY=ergierufhw894fhw49fh8w49fw4fwfoiejf
API_URL=127.0.0.1
API_PORT=80
POSTGRES_PORT=5432
POSTGRES_HOST=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=database

```

Create `.env.db` file for database:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=database

```

Create `.env.s3` file for MinIO S3 storage:

```
MINIO_ROOT_USER=test
MINIO_ROOT_PASSWORD=12345678

```

## Quickstart

Build & run project with docker-compose:

```bash
sudo docker-compose up -d --build
```

> [!NOTE]
> To access the documentation for the REST API, go to the application's URL `http://<url>/api/swagger`.
