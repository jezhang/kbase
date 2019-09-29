### 容器的状态和依赖

```sh
MAILER_CID=$(docker run -d dockerinaction/ch2_mailer)
WEB_CID=$(docker run -d nginx)
AGENT_CID=$(docker create --link $WEB_CID:insideweb \
    --link $MAILER_CID:insidemailer \
    dockerinaction/ch2_agent)
```

这个命令片段可以用来完成一个新的脚步，为每个客户启动新的NGINX和监控器实例

### 保存镜像(docker save)

```sh
docker pull busybox:latest
docker save -o myfile.tar busybox:latest
```


### 加载镜像(docker load)

```sh

```
