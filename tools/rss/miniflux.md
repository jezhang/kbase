

### Setup database


```sh
CREATE DATABASE miniflux;
```

### 4. Create user (change my_username and my_password)

```sh
CREATE USER dbuser WITH PASSWORD 'dbpass';
```

### 5. Grant privileges on database to user

```sh
GRANT ALL PRIVILEGES ON DATABASE "miniflux" to dbuser;
```


```sh
docker run -d \
  -p 8080:8080 \
  --name miniflux \
  --link postgres:db \
  -e "DATABASE_URL=postgres://miniflux:miniflux@db/miniflux?sslmode=disable" \
  -e "RUN_MIGRATIONS=1" \
  -e "CREATE_ADMIN=1" \
  -e "ADMIN_USERNAME=root" \
  -e "ADMIN_PASSWORD=pass" \
  docker.io/miniflux/miniflux:latest
```