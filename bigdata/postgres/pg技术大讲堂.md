
# 05数据库结构

## Postgres物理结构

## Postgres逻辑结构

## Postgres表空间结构(Tablespaces)

- PostgresaL中的表空问是基本目录之外的附加数据区域，此功能己在版本8.0中实现。
- 初始化数据库后默认的表空间有pg_default、pg_global。
- pg_global表空问的物理文件位置在数据目录的global目录中，它用水保存系统表。
- pg_default表空间的物理文件位置在数据目录的base子目录中，是templateO和template1
数据库的默认表空间。
- 创建数据库时，默认从template1数据库进行克隆，因此除非特别指定了新建数据库的表空间，否则默认使用template1使用的表空间，即pB_default表空间。

> 表空间的引入可以把数据库存放到不同的磁盘, base directory: `$PGDATA`

创建表空间时产生的目录命名规则

> PG_'Major version'_'Catalogue version number'

```
# create tablespace jezhang_tblspc location '/var/lib/postgresql/data/jezhang';
WARNING:  tablespace location should not be inside the data directory
CREATE TABLESPACE

# ls -la /var/lib/postgresql/data/jezhang/
total 12
drwx------  3 postgres postgres 4096 Dec  1 13:19 .
drwx------ 20 postgres root     4096 Dec  1 13:17 ..
drwx------  2 postgres postgres 4096 Dec  1 13:19 PG_16_202307071
```

```sql
select datname, oid, dattablespace from pg_database;
 postgres  |     5 |          1663
 template1 |     1 |          1663
 template0 |     4 |          1663
 sonar     | 16388 |          1663

select oid, spcname from pg_tablespace;
 1663 | pg_default
 1664 | pg_global
```

# 06用户与角色管理

```
postgres-# \du
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
 sonar     |

\d pg_user
 usename      | name                     |           |          |
 usesysid     | oid                      |           |          |
 usecreatedb  | boolean                  |           |          |
 usesuper     | boolean                  |           |          |
 userepl      | boolean                  |           |          |
 usebypassrls | boolean                  |           |          |
 passwd       | text                     |           |          |
 valuntil     | timestamp with time zone |           |          |
 useconfig    | text[]                   | C         |          |

select * from pg_user;
```

## 创建用户

```sh
CREATE USER user1 SUPERUSER CREATEDB LOGIN password 'password1'; 
```

## 创建角色

```sh
CREATE ROLE r1 LOGIN;
CREATE ROLE u4 encrypted PASSWORD '123456' VALID UNTIL '2023-12-31'
```

## 修改用户

```sh
ALTER USER u2 RENAME TO u22; # need createrole
ALTER USER u22 PASSWORD 'u22';
ALTER USER u22 CREATEROLE;
```
## 删除用户

```sh
DROPUSER -U postgres -p 7788 username;
DROP ROLE rolename;
DROP USER username;
DROP ROLE IF EXISTS role_name;
```




