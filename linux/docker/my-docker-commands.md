```sh

docker run -d nginx

docker exec -it <id/name> /bin/bash

docker stop <id/name>

docker ps

# 映射端口(宿主机/docker)
docker run -d -p 8080:80 nginx

# docker启动mysql
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql

# docker启动mysql命令行
docker exec -it mysql /bin/bash

docker run --name mysql -p 3308:3306 -v /root/mysql/:/var/lib/mysql/ -e MYSQL_ROOT_PASSWORD=root -d mysql

# 查看实时得的mysql log
docker logs mysql -f

# docker startup a wordpress process
docker run --name jezhang_wp -p 8881:80 --link mysql:mysql -v /root/jezhang_wp:/var/www/html -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_PASSWORD=root -d wordpress

# docker startup a nginx
docker exec -it nginx /bin/bash

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/conf.d -d nginx

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/conf.d \
            -v /root/nginx/tcp.d:/etc/nginx/tcp.d  -v /etc/letsencrypt:/etc/letsencrypt \
            -v /root/nginx/nginx.conf:/etc/nginx/nginx.conf:rw -d nginx

docker run --name nginx -p 80:80 -p 443:443 -v /root/nginx/conf.d:/etc/nginx/conf.d \
            -v /root/nginx/tcp.d:/etc/nginx/tcp.d -v /etc/letsencrypt:/etc/letsencrypt \
            -v /root/nginx/nginx.conf:/etc/nginx/nginx.conf:rw -v /root/downloads:/root -d nginx

# docker run letsencrypt generate a certificate
docker run -it --rm -p 443:443 -p 80:80 --name certbot \
            -v "/etc/letsencrypt:/etc/letsencrypt" \
            -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
            certbot/certbot certonly

# docker run redis
docker run --name redis -p 6379:6379 -v /root/redis/data:/data -d redis:latest
docker exec -it redis /bin/bash

# 装个ubuntu玩玩
# https://segmentfault.com/a/1190000009485188
docker run -t -i ubuntu:14.04 /bin/bash
docker run -v /root/downloads:/root -t -i ubuntu:16.04 /bin/bash
docker run --name ubuntu -d -v /root/downloads:/root -t -i ubuntu:16.04 /bin/bash
docker exec -it ubuntu /bin/bash


# suse linux 11
docker run --name suse11 -p 7080:8080 -p 50003:22 -v /root/my-docker-files:/root/jezhang -d -t -i  yuzhenpin/suse-11-sp3-x86_64-java /bin/bash

# docker local registry
docker run -d -p 5000:5000 -v /var/lib/registry:/var/lib/registry registry:2
docker push HOSTNAME:5000/image:tag --insecure-registry HOSTNAME
```