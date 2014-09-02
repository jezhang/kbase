Apache Maven笔记整理
====================
##Windows安装Maven##
[Apache Maven](http://maven.apache.org/)不需要安装为Windows服务，只需要下载一个Maven压缩包并解压到文件夹，并配置windows环境变量。

需要下载的软件：
  - JDK 1.6以上 [点击下载](http://www.oracle.com/technetwork/java/javase/archive-139210.html)
  - Maven 3.0.5 [点击下载](http://mirrors.hust.edu.cn/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.zip)

###1. JDK和JAVA_HOME环境变量设置###
首先把JDK安装好，设置环境变量:

![JAVA_HOME环境变量](img/java_home_env.png)

###2.Maven解压，MAVEN_HOME和path环境变量设置###
解压好Maven到硬盘，并设置环境变量

![MAVEN_HOME环境变量](img/maven_home_env.png)

![path环境变量](img/path.png)

###3.验证###
解压Maven并设置好环境变量后，在命令提示符输入"mvn -version"
```sh
C:\Users\jezhang>mvn -version
Apache Maven 3.0.5 (r01de14724cdef164cd33c7c8c2fe155faf9602da; 2013-02-19 21:51:28+0800)
Maven home: D:\Java\apache-maven-3.0.5\bin\..
Java version: 1.7.0_60, vendor: Oracle Corporation
Java home: D:\Java\jdk1.7.0_60\jre
Default locale: en_US, platform encoding: GBK
OS name: "windows 7", version: "6.1", arch: "x86", family: "windows"
```
如果你看到类似消息，证明你的Apache Maven已经成功安装到Windows

##如何启用Maven代理设置##
很多公司都设置了防火墙并且通过一台代理服务器让用户访问Internet，如果你在这样的公司，你需要手动设置代理服务器才能使用maven下载和管理依赖。

找到 %MAVEN_HOME%/conf/settings.xml，并找到下面这一段
```xml
    <!-- proxy
    Specification for one proxy, to be used in connecting to the network.
    <proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username>proxyuser</</username>
      <password>proxypass</password>
      <host>proxy.host.net</host>
      <port>80</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>-->
```
取消注释并设置你所在公司的代理服务器地址：
```xml
    <proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username></username>
      <password></password>
      <host>proxy.ap.signintra.com</host>
      <port>80</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>
```
保存settings.xml，你的Apache Maven现在应该能通过代理服务器连接Internet了。

[参考资料](http://maven.apache.org/guides/mini/guide-proxies.html)


##Maven本地库##
Maven本地库是一个本地文件夹用来保存你项目的所有依赖(插件,jar包和其它Maven下载的文件)。简单地说，当你build一个Maven项目，所有依赖文件都会保存到你的Maven本地库中。

Maven使用一个默认的文件夹：
  1. Unix/Mac OS X - ~/.m2
  2. Windows - C:\Documents and Settings\{your-username}\.m2

正常的我会更改这个默认设置，并且在本地建一个有意义的文件夹名称，例如：maven-repo。找到%MAVEN_HOME%\conf\settings.xml下面这一段代码：
```xml
  <!-- localRepository
   | The path to the local repository maven will use to store artifacts.
   |
   | Default: ~/.m2/repository
  <localRepository>/path/to/local/repo</localRepository>
  -->
<localRepository>D:/maven_repo</localRepository>
```
退出保存。你的本地Maven库已经改为 D:/maven_repo

##Maven中心库##
当你build一个Maven项目，Maven会检查你的"pom.xml"来确定哪些依赖需要下载。首先，Maven会先从本地库中获取依赖，如果没有找到，Maven会检查默认的Maven中心仓库 - <http://repo1.maven.org/maven/>，你在浏览器里尝试打开这个链接，你会发现这个站点已经无法打开，

好在Maven提供了<http://search.maven.org/>，现在好多了，你现在可以使用搜索功能了。虽然<http://repo1.maven.org/maven/>目录浏览功能被禁用，但是，当你build Maven项目时，它还是会从<http://repo1.maven.org/maven/>处获取依赖的，你可以查看Maven输出来验证。

##Maven远程库##
在Maven中，当你"pom.xml"中定义的包无法从Maven本地仓库或者Maven中心仓库下载时，进程将会停止并且会输出出错信息到Maven控制台。

例子：org.jvnet.localizer 在存在于 [Java.net repository](https://maven.java.net/content/repositories/public/)中。
```xml
    <dependency>
        <groupId>org.jvnet.localizer</groupId>
        <artifactId>localizer</artifactId>
        <version>1.8</version>
    </dependency>
```
当你build这个"pom.xml"时，会出现报错信息：
```bash
  Updated 12/12/2012
  The org.jvnet.localizer is now available in Maven center repository.
```
定义 Java.net 远程仓库，告诉Maven到java.net仓库中查找并下载依赖，在"pom.xml"中使用remote repository定义远程仓库：
```xml
    <repositories>
        <repository>
            <id>java.net</id>
            <url>https://maven.java.net/content/repositories/public/</url>
        </repository>
    </repositories>
```
现在，Maven会依照这样的顺序查找依赖：
  1.查找本地Maven仓库，如果没有找到，去执行第二步，否则退出；
  2.查找Maven中心仓库，如果没有找到，去执行第三步，否则退出；
  3.查找java.net远程Maven仓库，如果没有找到，提示报错信息，否则退出。

附加上Jboss远程仓库到"pom.xml"中：
```xml
    <repositories>
        <repository>
            <id>JBoss repository</id>
            <url>http://repository.jboss.org/nexus/content/groups/public/</url>
        </repository>
    </repositories>
```
[参考资料](http://maven2-repository.java.net/)

##Maven依赖机制，如何工作？##
Maven依赖机制会自动下载项目所必须依赖的包，同时维护依赖包的版本更新。

###例子学习###
让我们看一个例子来理解Maven是怎样工作的。假设你想使用Log4j作为你项目的logging机制。

  1. 使用传统方法
    1. 访问<http://logging.apache.org/log4j/>；
    2. 下载Log4j jar包；
    3. 复制jar包到项目classpath；
    4. 手动添加项目依赖；
    5. 所有事情都必须由你完成。
    6. 如果Log4j版本升级，你需要重复以上步骤
  2. 使用Maven
    1. 你需要知道log4j Maven coordinates, 例如：
    ```xml
        <groupId>log4j</groupId>
        <artifactId>log4j</artifactId>
        <version>1.2.14</version>
    ```
    它会自动下载log4j1.2.14版本，如果没有指定版本号，它会更新到最新版本。
    2. 在"pom.xml"中定义 Maven coordinates 
    ```xml
        <dependencies>
            <dependency>
                <groupId>log4j</groupId>
                <artifactId>log4j</artifactId>
                <version>1.2.14</version>
            </dependency>
        </dependencies>
    ```
    3. 当Maven编译或者打包时，log4j包会自动下载到Maven本地仓库中
    4. 所有工作有Maven完成。

如何查找Maven coordinates?
访问[Maven center repository](http://search.maven.org/)，查找你想要jar包的名称即可。

[参考资料](http://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)