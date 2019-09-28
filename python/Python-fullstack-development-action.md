Python 全栈开发实践入门
====================

## Sublime Text Plugin for Python

### Anaconda

编写python代码的时候提供代码提示

### AutoPEP8

安装PEP8规范检查代码格式的插件，帮助语法检查

### Emmet

HTML前端代码自动联想补全，输入头几个字母按Tab键会自动补全。输入英文格式的"!"并且按"Tab"键，

### Jinja2

Flash开发使用的Jinja模版，编辑html模版时候对jinja代码自动补全

### jquery

html前端jquery, ajax自动提示

### SideBarEnhancements

侧边栏增强，安装好后通过右击展开菜单

### SFTP

通过ssh协议实现远程编辑

### SublimeREPL

模拟交互式操作，类似IDLE操作


## Docker的安装与搭建

### 使用Docker搭建GitLab服务器

```sh
docker pull gitlab/gitlab-ce
docker run --detach \
    -- hostname 192.168.1.137 \  # 设置主机IP或域名
    -- publish 443:443 --publish 8000:8000 --publish 6050:22 \  # 绑定宿主机到容器的端口
    -- name gitlab \  # 定义容器别名
    -- volume /home/xyj/gitlab_volumn/config:/etc/gitlab \  # 将本地磁盘映射到容器内，用于持久保存Gitlab配置
    -- volume /home/xyj/gitlab_volumn/logs:/var/log/gitlab \  # 将本地磁盘映射到容器内，用于持久保存Gitlab运行日志
    -- volume /home/xyj/gitlab_volumn/data:/var/opt/gitlab \  # 将本地磁盘映射到容器内，用于持久保存Gitlab数据
    gitlab/gitlab-ce:latest  # 选择启动镜像

```

### 持续集成

```sh
git pull gitlab/gitlab-runner:latest
mkdir gitlab-ci_volumn
docker run -d --name c-gitlab-ci -v //home/xyj/gitlab-ci_volumn/config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/Docker.sock gitlab/gitlab-runner
```






















