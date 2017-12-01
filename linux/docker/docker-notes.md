DOCKER入门用法简介
==================

### 验证安装

```sh
docker run hello-world

# 分析上面指令结构：
# docker: 告诉操作系统，正在使用docker程序
# run: 子指令，创建并运行容器
# hello-world: 告诉docker哪个image被导入容器
```


### 查看container

从上面的指令可以知道，我们的docker已经安装成功了。我们可以用下面的命令查看自己正在运行的容器：

```sh
docker ps # 显示所有正在运行的容器
```

当然，也可能显示没有正在运行的容器（刚开始安装，还没有运行任何容器）。我们给它加个参数就能查看所有容器，包括没有运行的、正在运行的和运行过的。如下：

```sh
docker ps -a
```

这样就可以看到所有的容器，你一定能找到 hello-world这个运行过的容器。

### 镜像

镜像，就是一个文件系统，查看自己local的镜像命令：

```sh
docker images # 显示的是本地镜像
```

镜像保存到本地的好处：当加载image的时候，会直接在本地加载，不用去远程下载。节省时间，节省宽带。查找镜像地址： <https://store.docker.com/community/images/docker/whalesay>

> 镜像和容器的区别：容器只是镜像的一个实例，镜像被加载只是创建了一个实例。我们通过上面指令查看镜像，显示的可能比容器（docker ps -a） 要多。因为还有一些镜像只是下载在本地，却没有被加载，好比maven有个本地仓库。

### 删除容器

```sh
docker rm [id/name]

#删除所有
docker rm `docker ps -a -q`  #-q表示只返回容器的id
```

需要注意的是：上面的命令只是删除容器，不是删除镜像。

### 构建自己的镜像

首先创建一个Dockerfile文件，这个文件是一个菜单。由files,environment,commonds 来构建一个images.

#### 创建一个mydocker文件夹

```sh
mkdir mydocker
cd mydocker
```

#### 在新建目录下创建Dockerfile文件

```sh
touch Dcokerfile
vim Dockerfile
```

#### 开始编写Dockerfile

* 下面FROM指令的意思是，告诉Docker你要基于哪个镜像进行构建

```sh
FORM docker/whalesay:latest
```

* 下面RUN指令，给镜像安装一个软件fortunes(因为whalesay是基于ubuntu的，所以下面可以执行一些对象的指令)

```sh
RUN apt-get -y update && apt-get install fortunes
```

* 下面的CMD指令， 告诉镜像（这里是指成功后的镜像）最后需要去运行的指令

```sh
CMD /usr/games/fortune -a | cowsay
```

#### 好了，一切就绪。开始构建吧！

在Dockerfile同级目录下运行,用docker build 来构建，-t (tag)是给镜像一个tag，方便后面运行。表示Dockerfile在当前目录下

```sh
docker build -t jezhang-whale .
```

我们可以看看执行的打印输出，可以了解下详细的执行过程，成功会打印输出：Successfully built c5857....

#### 查看下自己构建的镜像

还记得怎么查看吗？对，你猜对了！就是用images来查看

```sh
docker images
```

### Docker Hub

#### 注册一个Docker Hub账户

在[Dockhub](https://hub.docker.com/)

#### 给你的images打上你的标志

在上传镜像之前，先给你的images打上你自己的标签吧！证明这是我的images，可能一不小心，你就出名了，哈哈！！！

> 账户名/镜像:版本

这里[账户名/]就是你的标签，官方给出的是，标签用你的docker hub账户名。给某个镜像打标签用 docker tag

```sh
docker tag c58570c0ad0d jezhang/jezhang-whale:latest

# docker tag 镜像id 新标签:版本

docker images # 查看
```

#### 登陆自己的账户

```sh
docker login
```

执行上面命令，然后输入你的账户名和密码，出现 Login Succeeded 登陆成功。

#### 开始push镜像

```sh
docker push jezhang/jezhang-whale
```

#### 删除本地镜像

```sh
docker rmi <id> 	# 你的id肯定跟这里不一样
docker rmi -f <id> 	# 强制删除
```

当然，刚开始学习，你的机器上估计也没有什么重要的镜像，应该都可以删除吧！清空！慎用！

```sh
docker rmi -f `docker images -a -q`
```

#### 体验下载自己容器的快乐

经历上面的删除镜像，相信你已经删除完那个上传的镜像。开始下载运行自己的镜像吧！怎么做？相信你没有忘记，就在最上面， 对！docker run ..

```sh
docker run jezhang/jezhang-whale
```

记得加上自己账户名，回车，开始下载。估计有点慢，因为我们上传到的是docker hub上，不是国内服务器。

> 这里再来回想一个问题：上面我们在上传镜像之前对自己的镜像打了tag，为什么要这么做？
在下载自己上传的镜像，相信你已经想到了，如果不加上自己账户名的话，那么大家都上传，要是遇到同名的镜像咋办！下载该下载谁的！加上自己的用户名，就是起一个namespace的作用，类似java里的包名作用。用户名是不会重复的，因为你注册的时候，保证了你的用户名具有唯一性。




