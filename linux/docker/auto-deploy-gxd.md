auto-deploy-gxd
===============

## Dcoker配置

```sh
sudo docker pull jenkins

mkdir /home/xxx/jenkins
cd /home/xxx/
sudo chown -R 1000:1000 jenkins/

sudo docker run -itd -p 8080:8080 -p 50000:50000 --name jenkins --privileged=true  -v /home/hzq/jenkins:/var/jenkins_home jenkins
# -p 8080:8080 -p 50000:50000 进行端口映射
# --privileged=true 在CentOS7中的安全模块selinux把权限禁掉了，参数给容器加特权。
# -v /home/hzq/jenkins:/var/jenkins_home

sudo dockers ps

# 在浏览器输入“localhost:8080”进入Jenkins，首次进入需要获取管理员的密码
# 获取密码方式一:
cat /home/xxx/jenkins/secrets/initialAdminPassword
# 获取密码方式二:
sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Create and run jenkins
docker run -itd -p 8080:8080 -p 50000:50000 --name jenkins --privileged=true -v /root/jenkins:/var/
jenkins_home jenkins

docker run --name jenkins --privileged=true -p 80:8080 -p 50000:50000 -p 50001:22 -e JAVA_OPTS="-Duser.timezone=Asia/Shanghai" -v /root/gxd/deployment/jenkins:/var/jenkins_home:rw jenkins

docker exec -it jenkins /bin/bash
docker exec -it -u root jenkins /bin/bash

# check password at /var/jenkins_home/secrets/initialAdminPassword
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

```


### ssh远程连接docker中的container

#### 安装ssh

```sh
sudo apt-get install openssh-server #安装ssh服务器
service ssh status # 查看ssh服务启动情况
service ssh start # 启动ssh服务
```

#### 配置ssh，允许root登陆
```sh
vi /etc/ssh/sshd_config
将PermitRootLogin的值从withoutPassword改为yes
```

#### 重启ssh服务
```sh
service ssh restart # 重启动ssh服务
```


## GXD Web部署脚本

```sh
deploy-web.sh 
# Sent incremental files to remote, upload deploy scripts, run SCN00001.sh on remote server
.deploy-scripts/SCN00001.sh # Use ant build, run cos.sh with user cos
.deploy-scripts/cos.sh # Copy the war to tomcat, and restart tomcat.
.deploy-scripts/runas.sh
```

## GXD Database script部署脚本

```sh
deploy-db.sh
.deploy-scripts/cos_ext.sh
```


## 备注

### How do I assign a port mapping to an existing Docker container?

```sh
# 1.stop running container
docker stop jenkins

# 2.commit the container
docker commit jenkins auto-deploy-gxd

# 3.re-run from the commited image
docker run -itd -p 8080:8080 -p 50000:50000 -p 50001:22 -e JAVA_OPTS="-Duser.timezone=Asia/Shanghai" --name gxd-jenkins --privileged=true -v /root/gxd/deployment/jenkins:/var/jenkins_home:rw gxd-jenkins


docker ps #查看正在运行的container
# **找到所要保存的container的container id，假设为xxxxxx**
docker commit xxxxxxxx tomjerry/foobar
# （注：tomjerry/foobar为要保存的新镜像的名字，可任意写）
```


