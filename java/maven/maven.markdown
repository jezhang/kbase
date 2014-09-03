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
    1. 你需要知道log4j Maven coordinates, 例如：log4j。它会自动下载指定版本，如果没有指定版本号，它会更新到最新版本。
    2. 在"pom.xml"中定义 Maven coordinate
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

##如何添加自定义类库到Maven本地仓库##
假如你写了一个jar包，名称叫"xxx"，你想把它加入到本地Maven库给其他人使用。
```sh
mvn install:install-file -Dfile=c:\xxx-{version}.jar -DgroupId=com.google.code 
-DartifactId=kaptcha -Dversion={version} -Dpackaging=jar
```
输出：
```sh
D:\>mvn install:install-file -Dfile=c:\xxx-2.0.jar -DgroupId=com.abc.code 
-DartifactId=xxx -Dversion=2.0 -Dpackaging=jar
[INFO] Scanning for projects...
[INFO] Searching repository for plugin with prefix: 'install'.
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Default Project
[INFO]    task-segment: [install:install-file] (aggregator-style)
[INFO] ------------------------------------------------------------------------
[INFO] [install:install-file]
[INFO] Installing c:\xxx-2.0.jar to 
D:\maven_repo\com\abc\code\xxx\2.0\xxx-2.0.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: < 1 second
[INFO] Finished at: Tue May 12 13:41:42 SGT 2009
[INFO] Final Memory: 3M/6M
[INFO] ------------------------------------------------------------------------
```
安装完成，只要在"pom.xml"中定义abc coordinate即可：
```xml
    <dependency>
        <groupId>com.google.code</groupId>
        <artifactId>kaptcha</artifactId>
        <version>2.3</version>
    </dependency>
```
构建，"xxx" jar包会从本地Maven库中获取到。


##如何使用Maven创建Java项目##
这一节，我们讲介绍如何使用Maven创建一个简单的Java项目，并让它支持Eclipse，而且打包到一个"jar"文件
###1. 从Maven模版建一个新项目###
```sh
mvn archetype:generate -DgroupId={project-packaging} -DartifactId={project-name} -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```
这行命令告诉Maven建一个Java项目，使用“**maven-archetype-quickstart**”模版，如果你忽略了```archetypeArtifactId```这个参数，将会列出一个模版列表供你选择。
请看样例：
```sh
$ mvn archetype:generate -DgroupId=info.woodchat -DartifactId=NumberGenerator -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] -- omitted for readability
[INFO] ----------------------------------------------------------------------------
[INFO] Using following parameters for creating project from Old (1.x) Archetype: maven-archetype-quickstart:1.0
[INFO] ----------------------------------------------------------------------------
[INFO] Parameter: groupId, Value: info.woodchat
[INFO] Parameter: packageName, Value: info.woodchat
[INFO] Parameter: package, Value: info.woodchat
[INFO] Parameter: artifactId, Value: NumberGenerator
[INFO] Parameter: basedir, Value: /Users/jezhang/Documents/workspace
[INFO] Parameter: version, Value: 1.0-SNAPSHOT
[INFO] project created from Old (1.x) Archetype in dir: /Users/jezhang/Documents/workspace/NumberGenerator
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 3.917s
[INFO] Finished at: Mon Dec 17 18:53:58 MYT 2012
[INFO] Final Memory: 9M/24M
[INFO] ------------------------------------------------------------------------
```
上面的例子，一个新的Java项目“NumberGenerator”和整个项目目录结构已经自动建好。
###2. Maven目录结构###
```java
NumberGenerator
   |-src
   |---main
   |-----java
   |-------com
   |---------jezhang
   |-----------App.java
   |---test
   |-----java
   |-------com
   |---------jezhang
   |-----------AppTest.java
   |-pom.xml
```
Maven建好标准的目录结构，更多信息请参考[官方文档](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)，简单地说，所有原文件存放在```/src/main/java/package```中，所有测试代码放在```/src/test/java/package```中。

是的，一个标准的```pom.xml```文件生成了，POM文件类似Ant```build.xml```文件，它规定了整个项目的信息，包含目录结构，项目插件和项目依赖，更多信息请参考[官方文档](http://maven.apache.org/guides/introduction/introduction-to-the-pom.html)
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>NumberGenerator</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>NumberGenerator</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```
###3. 和Eclipse一起工作###
```sh
mvn eclipse:eclipse
```
将会生成eclipse项目所需要的文件```.classpath```和```.project```。
```xml
<!-- file .classpath-->
<classpath>
  <classpathentry kind="src" path="src/test/java" 
           output="target/test-classes" including="**/*.java"/>
  <classpathentry kind="src" path="src/main/java" including="**/*.java"/>
  <classpathentry kind="output" path="target/classes"/>
  <classpathentry kind="var" path="M2_REPO/junit/junit/3.8.1/junit-3.8.1.jar" 
     sourcepath="M2_REPO/junit/junit/3.8.1/junit-3.8.1-sources.jar"/>
  <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER"/>
</classpath>

<!--file .project-->
<projectDescription>
  <name>jezhang-core</name>
  <comment/>
  <projects/>
  <buildSpec>
    <buildCommand>
      <name>org.eclipse.jdt.core.javabuilder</name>
    </buildCommand>
  </buildSpec>
  <natures>
    <nature>org.eclipse.jdt.core.javanature</nature>
  </natures>
</projectDescription>
```
打开Eclipse，File->Import->General->Existing Projects into Workspace->选择项目根目录->完成
###4. 更新POM###
默认的```pom.xml```非常简单，有时候你需要添加编译器插件告诉Maven使用哪种版本的JDK来编译你的项目(默认JDK1.4)

```XML
  <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>2.3.2</version>
    <configuration>
      <source>1.6</source>
      <target>1.6</target>
    </configuration>
  </plugin>
```
更新jUnit从3.8.1到4.11
```xml
  <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.11</version>
    <scope>test</scope>
  </dependency>
```
POM完整的版本
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>NumberGenerator</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>NumberGenerator</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
 
  <build>
    <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>2.3.2</version>
      <configuration>
        <source>1.6</source>
        <target>1.6</target>
      </configuration>
    </plugin>
    </plugins>
  </build>
 
</project>
```
再次在命令提示符里输入```mvn eclipse:eclipse```，Maven会自动下载插件和依赖并保存到本地Maven仓库中。
###5.  更新业务逻辑###
测试驱动开发(TDD)，首先更新单元测试类，让App对象有一个方法生成一个唯一的key包含36个字符
```java
// AppTest.java
package info.woodchat;
import org.junit.Assert;
import org.junit.Test;
public class AppTest {
  @Test
  public void testLengthOfTheUniqueKey() {
    App obj = new App();
    Assert.assertEquals(36, obj.generateUniqueKey().length()); 
  }
}
```
在生产类完成业务逻辑代码：
```java
// App.java
package info.woodchat;
import java.util.UUID;
/**
 * Generate a unique number
 */
public class App {
    public static void main( String[] args ){
        App obj = new App();
        System.out.println("Unique ID : " + obj.generateUniqueKey());
    } 
    public String generateUniqueKey(){ 
      String id = UUID.randomUUID().toString();
      return id; 
    }
}
```
###6.Mave打包###
现在，我们要使用Maven编译这个项目并且打包到一个“jar”文件。根据```pom.xml```文件中```packging```元素定义的格式和输出
```xml
<!--pom.xml - full version.-->
<project ...>
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>NumberGenerator</artifactId> 
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
</project>
```
在命令提示符输入```mvn package```
```sh
$pwd
/Users/jezhang/Documents/workspace/NumberGenerator
 
$ mvn package
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building NumberGenerator 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO] ...omitted for readability
 
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running info.woodchat.AppTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.078 sec
 
Results :
 
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
 
[INFO] 
[INFO] --- maven-jar-plugin:2.3.1:jar (default-jar) @ NumberGenerator ---
[INFO] Building jar: /Users/jezhang/Documents/workspace/NumberGenerator/target/NumberGenerator-1.0-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 3.064s
[INFO] Finished at: Mon Dec 17 23:38:05 MYT 2012
[INFO] Final Memory: 15M/135M
[INFO] ------------------------------------------------------------------------
```


##如何用Maven建一个Web项目##
在这个教程中，我将演示如何使用Maven建一个Java Web Application(with Spring MVC)项目，并且支持Eclipse

###1. 从Maven模版建Web Application项目###
在terminal或者命令提示符输入一下命令：
```sh
mvn archetype:generate -DgroupId={project-packaging} -DartifactId={project-name} -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```
这条命令告诉maven使用“**maven-archetype-webapp**”模版新建一个Java web application项目
> 例如
```sh
$ pwd
/Users/jezhang/Documents/workspace
 
$ mvn archetype:generate -DgroupId=info.woodchat -DartifactId=CounterWebApp -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false

[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Stub Project (No POM) 1
[INFO] ------------------------------------------------------------------------
[INFO] 
[INFO] Generating project in Batch mode
[INFO] ----------------------------------------------------------------------------
[INFO] Using following parameters for creating project from Old (1.x) Archetype: maven-archetype-webapp:1.0
[INFO] ----------------------------------------------------------------------------
[INFO] Parameter: groupId, Value: info.woodchat
[INFO] Parameter: packageName, Value: info.woodchat
[INFO] Parameter: package, Value: info.woodchat
[INFO] Parameter: artifactId, Value: CounterWebApp
[INFO] Parameter: basedir, Value: /Users/jezhang/Documents/workspace
[INFO] Parameter: version, Value: 1.0-SNAPSHOT
[INFO] project created from Old (1.x) Archetype in dir: /Users/jezhang/Documents/workspace/CounterWebApp
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 3.147s
[INFO] Finished at: Thu Dec 20 20:35:19 MYT 2012
[INFO] Final Memory: 12M/128M
[INFO] ------------------------------------------------------------------------
```

在上面的案例中，一个名为“**CounterWebApp**”web application项目被自动建好了，包含整个项目目录结构
###2. Maven目录布局设计###
Maven建好web application目录结构，并且建好一个标准的部署描述符```web.xml```和一个Maven```pom.xml```

```java
CounterWebApp
   |-src
   |---main
   |-----resources
   |-----webapp
   |-------index.jsp
   |-------WEB-INF
   |---------web.xml
   |-pom.xml
```
> 更多详细信息请参考[官方文档](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
```xml
<!--pom.xml-->
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>CounterWebApp</artifactId>
  <packaging>war</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>CounterWebApp Maven Webapp</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <finalName>CounterWebApp</finalName>
  </build>
</project>

<!--web.xml Servlet 2.3 太旧，建议升级到2.5-->
<!DOCTYPE web-app PUBLIC
 "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
 "http://java.sun.com/dtd/web-app_2_3.dtd" >
 
<web-app>
  <display-name>Archetype Created Web Application</display-name>
</web-app>

<!--index.jsp -- 一个简单的hello world html文件-->
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
```
###3. 支持Eclipse编辑器###
转换Maven web application项目到Eclipse支持的项目，输入一下命令：
```sh
mvn eclipse:eclipse -Dwtpversion=2.0
```
你必须在尾部加上```-Dwtpversion=2.0```参数说明这是一个Eclipse web项目。
> 注意！许多用户会疑惑，如果你只输入```mvn eclipse:eclipse```，它只能把该项目转换成Eclipse java项目，加上```-Dwtpversion=2.0``` 参数才能转换成Eclipse web项目

###4. 更新POM###
想要让上面的项目支持Spring MVC框架，我们需要修改```pom.xml```
1. 添加JDK6编译器
2. 添加Spring框架依赖
3. 升级jUnit到4.11
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>CounterWebApp</artifactId>
  <packaging>war</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>CounterWebApp Maven Webapp</name>
  <url>http://maven.apache.org</url>
 
  <properties>
    <spring.version>3.0.5.RELEASE</spring.version>
    <junit.version>4.11</junit.version>
    <jdk.version>1.6</jdk.version>
  </properties>
 
  <dependencies> 
    <!-- Spring 3 dependencies -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>${spring.version}</version>
    </dependency>
 
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>${spring.version}</version>
    </dependency>
 
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>${spring.version}</version>
    </dependency>
 
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>${junit.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <finalName>CounterWebApp</finalName>
    <plugins>
      <plugin>        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.0</version>
        <configuration>
          <source>${jdk.version}</source>
          <target>${jdk.version}</target>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```
###5. Spring MVC REST###
新建一个Spring MVC控制器类，有2个简单的方法(打印消息)
```java
/*/src/main/java/info/woodchat/controller/BaseController.java*/
package info.woodchat.controller; 
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
 
@Controller
@RequestMapping("/")
public class BaseController {
  @RequestMapping(value="/welcome", method = RequestMethod.GET)
  public String welcome(ModelMap model) { 
    model.addAttribute("message", "Maven Web Project + Spring 3 MVC - welcome()"); 
    //Spring uses InternalResourceViewResolver and return back index.jsp
    return "index"; 
  } 
  @RequestMapping(value="/welcome/{name}", method = RequestMethod.GET)
  public String welcomeName(@PathVariable String name, ModelMap model) { 
    model.addAttribute("message", "Maven Web Project + Spring 3 MVC - " + name);
    return "index"; 
  } 
}
```
新建一个Spring配置文件来定义Spring视图分解器
```xml
<!--/src/main/webapp/WEB-INF/mvc-dispatcher-servlet.xml-->
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:context="http://www.springframework.org/schema/context"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
        http://www.springframework.org/schema/beans     
        http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
        http://www.springframework.org/schema/context 
        http://www.springframework.org/schema/context/spring-context-3.0.xsd"> 
  <context:component-scan base-package="info.woodchat.controller" />
 
  <bean   class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix">
      <value>/WEB-INF/pages/</value>
    </property>
    <property name="suffix">
      <value>.jsp</value>
    </property>
  </bean> 
</beans>
```
更新```web.xml```支持Servlet 2.5，并且集成Spring框架到此web application项目(通过 Spring's listener```ContextLoaderListener```)
```xml
<!--/src/main/webapp/WEB-INF/web.xml-->
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"       xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" version="2.5"> 
  <display-name>Counter Web Application</display-name> 
  <servlet>
    <servlet-name>mvc-dispatcher</servlet-name>
    <servlet-class>     org.springframework.web.servlet.DispatcherServlet
    </servlet-class>
    <load-on-startup>1</load-on-startup>
  </servlet> 
  <servlet-mapping>
    <servlet-name>mvc-dispatcher</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping> 
  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/mvc-dispatcher-servlet.xml</param-value>
  </context-param> 
  <listener>
    <listener-class>      org.springframework.web.context.ContextLoaderListener
    </listener-class>
  </listener>
</web-app>
```
把```index.jsp```移动到```WEB-INF```目录里面，以保护用户直接访问，另外，修改此文件打印出从控制器出过来的变量```${message}```
```html
<!--/src/main/webapp/WEB-INF/pages/index.jsp-->
<html>
<body>
<h2>Hello World!</h2>
 
<h4>Message : ${message}</h1> 
</body>
</html>
```
###6. Eclipse + Tomcat###
为了让启动和调试此项目通过Eclipse server插件(Tomcat等)。你需要再次输入一下命令
```sh
mvn eclipse:eclipse -Dwtpversion=2.0
```
> 重要！
> 许多开发人员在这里发生问题，他们无法执行启动和调试在Eclipse server插件里面，错误消息是“依赖无法找到”，右击你的项目点属性，确保所有的依赖关系部署在组件内。否则运行```mvn eclipse:eclipse -Dwtpversion=2.0```
###7. Maven打包###
再次打开```pom.xml```，```packaging```定义了格式和输出
```xml
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat</groupId>
  <artifactId>CounterWebApp</artifactId> 
  <packaging>war</packaging>
  <version>1.0-SNAPSHOT</version>
```
打包成一个部署项目很简单，只要输入```mvn package```命令，它将会编译和打包web项目到一个"war"文件存在```project/target```文件夹
```sh
/Users/jezhang/Documents/workspace/CounterWebApp
 
Yongs-MacBook-Air:CounterWebApp jezhang$ mvn package
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building CounterWebApp Maven Webapp 1.0-SNAPSHOT
[INFO] ------------------------------------------------------------------------
[INFO] -- omitted for readability
[INFO] 
[INFO] --- maven-war-plugin:2.1.1:war (default-war) @ CounterWebApp ---
[INFO] Packaging webapp
[INFO] Assembling webapp [CounterWebApp] in [/Users/jezhang/Documents/workspace/CounterWebApp/target/CounterWebApp]
[INFO] Processing war project
[INFO] Copying webapp resources [/Users/jezhang/Documents/workspace/CounterWebApp/src/main/webapp]
[INFO] Webapp assembled in [87 msecs]
[INFO] Building war: /Users/jezhang/Documents/workspace/CounterWebApp/target/CounterWebApp.war
[INFO] WEB-INF/web.xml already added, skipping
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 3.936s
[INFO] Finished at: Thu Dec 20 22:28:53 MYT 2012
[INFO] Final Memory: 14M/206M
[INFO] ------------------------------------------------------------------------
```
完成，拷贝```project/target/CounterWebApp.war```并部署到你的容器。
###8. Demo###
启动web项目
<http://localhost:8080/CounterWebApp/welcome>

