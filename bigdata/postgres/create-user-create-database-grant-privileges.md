# PostgreSQL — Create User, Create Database, Grant privileges/access

Let’s assume that you’ve already have PostgreSQL installed on your Ubuntu machine and that you want to create a user, create a database and grant the user privileges to write/read to/from the database. The following steps should cover that:

### 1. Switch to postgres user

```sh
sudo su postgres
```

### 2. Enter the the interactive terminal for working with Postgres

```sh
psql
```

### 3. Create the database (change database_name)

```sh
CREATE DATABASE database_name;
```

### 4. Create user (change my_username and my_password)

```sh
CREATE USER my_username WITH PASSWORD 'my_password';
```

### 5. Grant privileges on database to user

```sh
GRANT ALL PRIVILEGES ON DATABASE "database_name" to my_username;
```

Happy hacking...