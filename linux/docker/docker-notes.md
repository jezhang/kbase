DOCKER USAGE
============

```sh
docker run -d nginx
docker exec -it 4c53b9 bash
docker stop 4c53b9d970ac
docker ps
docker run -d -p 8080:80 nginx
# docker启动mysql
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql
# docker启动mysql命令行
docker exec -it mysql /bin/bash
docker run --name mysql -p 3306:3306 -v /root/databases/:/var/lib/mysql/ -e MYSQ                                                                                        L_ROOT_PASSWORD=root -d mysql
docker logs mysql
# docker startup a wordpress process
docker run --name jezhang_wp -p 8881:80 --link mysql:mysql -v /root/jezhang_wp:/                                                                                        var/www/html -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_PASSWORD=root -d wordpre                                                                                        ss

# docker startup a nginx
docker exec -it nginx /bin/bash

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/con                                                                                        f.d -d nginx

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/con                                                                                        f.d -v /root/nginx/tcp.d:/etc/nginx/tcp.d  -v /etc/letsencrypt:/etc/letsencrypt                                                                                          -v /root/nginx/nginx.conf:/etc/nginx/nginx.conf:rw -d nginx

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/conf.d -v /root/nginx/tcp.d:/etc/nginx/tcp.d -v /etc/letsencrypt:/etc/letsencrypt -v /root/nginx/nginx.conf:/etc/nginx/nginx.conf:rw -v /root/downloads:/root/downloads -d nginx

# docker generate a certificate
docker run -it --rm -p 443:443 -p 80:80 --name certbot \
            -v "/etc/letsencrypt:/etc/letsencrypt" \
            -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
            certbot/certbot certonly


# 装个ubuntu玩玩
# https://segmentfault.com/a/1190000009485188
docker run -t -i ubuntu:14.04 /bin/bash
docker run --name ubuntu -v /root/downloads:/root/downloads -t -i ubuntu:14.04 /bin/bash

```
