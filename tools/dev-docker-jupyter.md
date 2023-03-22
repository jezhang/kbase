使用Docker安装配置Jupyter
=======================

## 前言

## 安装jupyter

1、登录dockerhub查看需要的Jupyter - Docker Official Images。

2、下载jupyter镜像（以6.1.1为例）
```sh
docker pull jupyter/base-notebook:notebook-5.7.8
```
注意不要使用6.x.x，存在页面无法显示扩展插件的bug，详情参考Jupyter nbextensions_configurator not shown。

3、创建配置目录

```sh
mkdir -p /home/ubuntu/jupyter/jovyan
mkdir -p /home/ubuntu/jupyter/jovyan/.jupyter
chmod 777 -R /home/ubuntu/jupyter/jovyan
```

4、启动jupyter服务

```sh
docker run --name vk-jupyter -d \
-p 8888:8888 \
-v /home/ubuntu/jupyter/jovyan:/home/jovyan \
jupyter/base-notebook
```

以上命令：

 - 命名容器为vk-jupyter，后台运行
 - 映射宿主机8888端口到容器的8888端口
 - 挂载宿主机目录/opt/jupyter/jovyan到容器目录/home/jovyan

5、验证安装
docker ps，jupyter启动正常的话就可以看到vk-jupyter容器。

6、登录
```sh
docker exec -it vk-jupyter jupyter notebook list
```
可以查看到登录需要的token，使用token即可登录进入jupyter编辑页面。

## 配置jupyter

### 1、设置密码

```sh
docker exec -it vk-jupyter jupyter notebook password
docker restart vk-jupyter
```

### 2、使用密码

浏览器访问 http://192.168.56.130:8888
此时使用自己设置的密码就可以访问jupyter了。

### 3、根目录

jupyter编辑器的默认根目录为 /home/jovyan ，对应宿主机目录 /opt/jupyter/jovyan ，创建的目录和文件都去这个路径下面去找。

### 4、安装ipywidgets

```sh
docker exec -it vk-jupyter pip install ipywidgets
```

## 配置Nginx

jupyter 使用了 websocket 协议，所以需要配置支持 websocket。
如果不配置的话，通过域名访问时会报错无法连接内核，也就无法运行python脚本。

```sh
server {
    listen 80;
    server_name jupyter.voidking.com;
    charset utf-8;
    location /{
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header  X-Forwarded-For  $proxy_add_x_forwarded_for;

        proxy_pass http://172.17.12.85:8888;

        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## jupyter小技巧

### 执行bash

在代码框里输入叹号+bash命令，即可执行bash，例如：

```sh
!ls -l
```

### 登录进容器

```sh
docker exec -it vk-jupyter /bin/bash
docker exec --user root -it vk-jupyter /bin/bash
```

### 安装常用命令

```sh
docker exec --user root -it vk-jupyter /bin/bash
apt update
apt install curl
apt install unzip
```

### 安装插件

Jupyter Notebook 扩展插件（nbextensions）是一些 JavaScript 模块，我们可以使用插件强化 Notebook 的功能。扩展插件本质上修改了 Jupyter UI，以实现更强大的功能。

1、界面添加 Nbextensions

```sh
docker exec -it vk-jupyter conda install -c conda-forge jupyter_nbextensions_configurator
#docker exec -it vk-jupyter pip install jupyter_nbextensions_configurator -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
docker exec -it vk-jupyter jupyter nbextensions_configurator enable --user
docker exec -it vk-jupyter jupyter nbextension list
docker restart vk-jupyter
```

2、安装常用扩展集合

```sh
docker exec -it vk-jupyter pip install jupyter_contrib_nbextensions -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
#docker exec -it vk-jupyter conda install -c conda-forge jupyter_contrib_nbextensions
docker exec -it vk-jupyter jupyter contrib nbextension install --user
docker exec -it vk-jupyter jupyter nbextension list
```




