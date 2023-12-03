
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

# 06 Postgres用户与schema对应关系

## Schema概念

- 用户的对象的集合叫做schema
- 可以把用户拥有的对象根据业务分类，不同的对象存放在不同的模式下
- 新建的数据库默认会创建不同的模式来管理对象。e.g. information_schema, pg_catalog, pg_temp_1, pg_toast, pg_toast_temp_1, public等
- 不同的schema下可以有相同名字的表、试图或函数等对象，相互之间不冲突，只有要权限，每个schema的对象是可以相互调用的

## user与schema的对应关系

- 一个用户可以创建和拥有多个模式
- 一个模式智能属于一个用户
- 普通用户创建模式时需要授权在指定的数据库下创建模式的权限

```sql
CREATE DATABASE testdb;
CREATE USER u1 PASSWORD 'u1';
GRANT CREATE ON DATABASE testdb TO u1;
GRANT USAGE ON SCHEMA sch_name TO role_name;
GRANT SELECT ON sch_name.tab_name to role_name;
```

## Public schema

### 搜索路径设置

```
show search_path;
set search_path="$user", public, scott;
```

## Schema管理



