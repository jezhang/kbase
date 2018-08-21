Install Squid Proxy inside Docker
=================================


```sh
docker run --name squid -d -p 8213:3128 -v /srv/docker/squid/cache:/var/spool/squid sameersbn/squid:3.5.27
docker exec -it squid /bin/bash

apt-get update
apt-get install vim
apt-get install apache2

/etc/init.d/squid stop
cd /etc/squid/
mv squid.conf squid.conf.bak
htpasswd -c /etc/squid/passwd jezhang
touch squid.conf
vim squid.conf
```sh


squid.conf
=========================================================================
http_port 3128
#acl OverConnLimit maxconn 200
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm DBSchenker Squid Server
auth_param basic credentialsttl 12 hours
acl auth_user proxy_auth REQUIRED
#http_access deny OverConnLimit
http_access allow auth_user
http_access deny all

cache_mem 128 MB
maximum_object_size 16 MB
cache_dir ufs /var/spool/squid 100 16 256
access_log /var/log/squid/access.log
visible_hostname www.dbschenker.com
cache_mgr 3411198@qq.com
=========================================================================
