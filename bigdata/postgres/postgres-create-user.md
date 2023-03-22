## How to grant a user with only DDL privilege?

To grant a user with only DDL privilege, you can use the following command:

```sh
GRANT USAGE, CREATE ON SCHEMA schema_name TO user_name;
```

This will grant the user with the ability to create objects in the specified schema. If you want to grant the user with the ability to modify or delete objects, you can use the following command:

```sh
GRANT USAGE, CREATE, ALTER, DROP ON SCHEMA schema_name TO user_name;
```

Note that the above commands only grant privileges on the specified schema. If you want to grant privileges on specific tables or sequences, you can use the following command:

```sh
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE table_name TO user_name;
GRANT USAGE, SELECT, UPDATE ON SEQUENCE sequence_name TO user_name;
```

Replace schema_name, user_name, table_name, and sequence_name with the appropriate values.

## How to define a db user with only DML privileges on specified schema?

To define a db user with only DML privileges on a specified schema, you can use the following command:

```sh
GRANT USAGE, SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO user_name;
```

This will grant the user with the ability to perform DML operations on all tables in the specified schema. If you want to grant the user with the ability to perform DDL operations as well, you can use the following command:

```sh
GRANT USAGE, SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP ON SCHEMA schema_name TO user_name;
```

Replace schema_name and user_name with the appropriate values.

## How to grant a db user with only readonly permission with specified schema?

To grant a db user with only readonly permission on a specified schema, you can use the following command:

```sh
GRANT USAGE, SELECT ON ALL TABLES IN SCHEMA schema_name TO user_name;
```

This will grant the user with the ability to perform SELECT operations on all tables in the specified schema.

Replace schema_name and user_name with the appropriate values.