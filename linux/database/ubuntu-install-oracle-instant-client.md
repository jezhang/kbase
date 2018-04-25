Ubuntu安装Oracle Instant Client
===============================


### 一、安装Oracle Instant Client

#### 1、下载Oracle client，在这里[下载](http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html)，需要下载3个RPM的包；

#### 2、安装alien，和依赖包

```sh
$ sudo apt-get install alien
$ sudo apt-get install libaio1
```

#### 3、使用alien吧rpm包转换成deb包，并且安装：

```sh
$ sudo alien -i oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm
$ sudo alien -i oracle-instantclient11.2-devel-11.2.0.4.0-1.x86_64.rpm
$ sudo alien -i oracle-instantclient11.2-sqlplus-11.2.0.4.0-1.x86_64.rpm
```

> 一般会安装在/usr/lib/oracle/11.2/client64目录下

#### 4、设置环境变量：vim ~/.bashrc，在最后添加以下内容

```sh
export ORACLE_HOME=/usr/lib/oracle/11.2/client64
export LD_LIBRARY_PATH=/usr/lib/oracle/11.2/client64/lib
export TNS_ADMIN=/usr/lib/oracle/11.2/client64/network/admin
export PATH=$PATH:$ORACLE_HOME/bin
```

> 在Ubuntu11.10和14.04测试,就需要添加PATH=$PATH:$ORACLE_HOME/bin，如果注释PATH变量则会提示没有‘sqlplus’命令；网上也有人说不需要；

#### 5、添加文件：sudo vim /etc/ld.so.conf.d/oracle.conf 并加入以下内容

```sh
/usr/lib/oracle/11.2/client64/lib/
```

然后执行命令

```sh
sudo ldconfig
```

#### 6、重新打开终端，输入sqlplus /nolog；就可以进SQL了

#### 7、在/usr/lib/oracle/11.2/client64/目录添加tnsnames.ora文件

```sh
cd /usr/lib/oracle/11.2/client64
sudo mkdir network
cd network
sudo mkdir admin
cd admin
sudo vim tnsnames.ora
```

> 在tnsnames.ora添加的内容，注意：内容不能少；

```sh
ORCL =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.88.71)(PORT = 1521))
    )   
    (CONNECT_DATA =
      (SERVICE_NAME = orcl)
    )   
  )
```

并修改权限：sudo chmod a+w \*.ora

#### 8、进人sqlplus不能使用上下键查看历史命令，安装rlwrap解决

```sh
$ sudo apt-get install rlwrap
````

在~/.bashrc中添加别名

```sh
alias sqlplus='rlwrap sqlplus'
```

重新打开终端，进人sqlplus则可以使用上下键了；


### 二、安装cx_Oracle，可以使用Python链接数据库

#### 1、下载安装cx_Oracle，在这里下载，注意对应的Python、Oracle client版本，我用的是：cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm

```sh
pip install cx_Oracle
```

#### 2、解压cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm，并把cx_Oracle.so文件复制到python的目录，这里为：/usr/local/lib/python2.7/dist-packages

#### 3、测试链接

```python
import cx_Oracle

conn = cx_Oracle.connect("username/password@192.168.1.xxx:1521/orcl")
print conn.version
conn.close()
```

运行该脚本后，可以打印出Oracle的版本；