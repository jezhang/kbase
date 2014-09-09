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
这条命令告诉maven使用“**maven-archetype-webapp**”模版新建一个Java web application项目，例如：

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
      <plugin><groupId>org.apache.maven.plugins</groupId>
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
 
  <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
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
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" version="2.5"> 
  <display-name>Counter Web Application</display-name> 
  <servlet>
    <servlet-name>mvc-dispatcher</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
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
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
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


##如何使用Maven模版创建项目##
Maven拥有多余40种模版方便开发者快速创建Java项目。通过下面的步骤来创建Java项目，Maven命令"```mvn archetype:generate```"

###1. Maven - mvn archetype:generate###
如果你运行此不带任何参数的命令，Maven控制台将会变成交互模式：
```sh
jezhang@SSC1-W217 /e/kbase/java/maven/example (master)
$ mvn archetype:generate
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Stub Project (No POM) 1
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] >>> maven-archetype-plugin:2.2:generate (default-cli) @ standalone-pom >>>
[INFO]
[INFO] <<< maven-archetype-plugin:2.2:generate (default-cli) @ standalone-pom <<<
[INFO]
[INFO] --- maven-archetype-plugin:2.2:generate (default-cli) @ standalone-pom ---
[INFO] Generating project in Interactive mode
```

一会儿后Maven将会列出上千条archetype供你选择：

```sh
... ... ...
... ... ...
1069: remote -> org.wikbook:wikbook.archetype (-)
1070: remote -> org.wildfly.archetypes:wildfly-subsystem (An archetype that generates a skeleton project for implementing a WildFly 8 subsystem)
1071: remote -> org.wiperdog:wiperdog-osgi-bundle-archetype (-)
1072: remote -> org.wiperdog:wiperdog-osgi-ipojo-archetype (-)
1073: remote -> org.wisdom-framework:wisdom-default-project-archetype (-)
1074: remote -> org.wisdom-framework:wisdom-simple-watcher-archetype (-)
1075: remote -> org.xaloon.archetype:xaloon-archetype-wicket-jpa-glassfish (-)
1076: remote -> org.xaloon.archetype:xaloon-archetype-wicket-jpa-spring (-)
1077: remote -> org.xwiki.commons:xwiki-commons-component-archetype (Make it easy to create a maven project for creating XWiki Components.)
1078: remote -> org.xwiki.rendering:xwiki-rendering-archetype-macro (Make it easy to create a maven project for creating XWiki Rendering Macros.)
1079: remote -> org.zkoss:zk-archetype-component (An archetype that generates a starter ZK component project)
1080: remote -> org.zkoss:zk-archetype-extension (An archetype that generates a starter ZK extension project)
1081: remote -> org.zkoss:zk-archetype-theme (An archetype that generates a starter ZK theme project)
1082: remote -> org.zkoss:zk-archetype-webapp (An archetype that generates a starter ZK CE webapp project)
1083: remote -> org.zkoss:zk-ee-eval-archetype-webapp (An archetype that generates a starter ZK EE-eval webapp project)
1084: remote -> org.zkoss:zk-ee-eval-archetype-webapp-spring (An archetype that generates a starter ZK EE-eval webapp project with Spring)
1085: remote -> org.zkoss:zk-ee-eval-archetype-webapp-spring-jpa (An archetype that generates a starter ZK EE-eval webapp project with Spring and JPA)
1086: remote -> pl.bristleback:webapp-archetype (Web archetype for Bristleback Websocket Framework)
1087: remote -> pro.savant.circumflex:webapp-archetype (-)
1088: remote -> ru.circumflex:circumflex-archetype (-)
1089: remote -> ru.nikitav.android.archetypes:release (-)
1090: remote -> ru.nikitav.android.archetypes:release-robolectric (-)
1091: remote -> ru.stqa.selenium:webdriver-java-archetype (Archetype for a Maven project intended to develop tests with Selenium WebDriver and JUnit/TestNG)
1092: remote -> ru.stqa.selenium:webdriver-junit-archetype (Archetype for a Maven project intended to develop tests with Selenium WebDriver and JUnit)
1093: remote -> ru.stqa.selenium:webdriver-testng-archetype (Archetype for a Maven project intended to develop tests with Selenium WebDriver and TestNG)
1094: remote -> se.vgregion.javg.maven.archetypes:javg-minimal-archetype (-)
1095: remote -> sk.seges.sesam:sesam-annotation-archetype (-)
1096: remote -> tk.skuro:clojure-maven-archetype (A simple Maven archetype for Clojure)
1097: remote -> tr.com.lucidcode:kite-archetype (A Maven Archetype that allows users to create a Fresh Kite project)
1098: remote -> uk.ac.rdg.resc:edal-ncwms-based-webapp (-)
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains): 439:
```
此时你可以输入一个数字或者一个关键字用来过滤，我们敲入"spring"：

```sh
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains): 439: spring
Choose archetype:
1: remote -> co.ntier:spring-mvc-archetype (An extremely simple Spring MVC archetype, configured with NO XML.)
2: remote -> com.cloudfoundry.tothought:spring-data-basic (A basic setup for Spring Data + Hibernate + MySql)
3: remote -> com.force.sdk:springmvc-archetype (-)
4: remote -> com.github.akiraly.reusable-poms:simple-java-project-with-spring-context-archetype (-)
5: remote -> com.github.akiraly.reusable-poms:simple-java-project-with-spring-hibernate-querydsl-archetype (-)
6: remote -> com.graphaware.neo4j:graphaware-springmvc-maven-archetype (-)
7: remote -> com.graphaware.neo4j:neo4j-springmvc-maven-archetype (-)
8: remote -> com.lordofthejars.thymeleafarchetype:thymeleaf-spring-maven-archetype (Thymeleaf Spring Maven Archetype)
9: remote -> com.mikenimer:extjs-springmvc-webapp (A maven Archetype to create new EXTJS project powered by a spring MVC service.)
10: remote -> eu.vitaliy:java6se-spring3-archetype (Simple spring 3 archetype)
11: remote -> io.fabric8.archetypes:camel-spring-boot-archetype (Shows how to use Camel with Spring Boot in the Java Container.)
12: remote -> io.fabric8.archetypes:camel-spring-java-archetype (Creates a new Camel Spring project which uses the Java Container in Fabric8.)
13: remote -> io.fabric8.archetypes:java-camel-spring-archetype (Creates a new Shows how to use Camel and CDI in a WAR)
14: remote -> io.fabric8.archetypes:spring-boot-webmvc-archetype (Shows how to use Spring Boot with WebMVC in the Java Container)
15: remote -> io.fabric8.archetypes:springboot-activemq-archetype (Creates a new Shows how to use ActiveMQ with Spring Boot in the Java Container)
16: remote -> io.fabric8.archetypes:springboot-camel-archetype (Creates a new Shows how to use Camel with Spring Boot in the Java Container)
17: remote -> io.fabric8.archetypes:springboot-webmvc-archetype (Creates a new Shows how to use Spring Boot with WebMVC in the Java Container)
18: remote -> it.cosenonjaviste:jsf2-spring4-jpa2-archetype (This archetype is based on org.fluttercode.knappsack/spring-jsf-jpa-archetype/1.1 one.
This new archetype upgrade libraries to JSF 2.2, Spring 4 and JPA 2.1)
19: remote -> ml.rugal.archetype:springmvc-spring-hibernate (A pretty useful JavaEE application archetype based on springmvc spring and hibernate)
20: remote -> org.apache.camel.archetypes:camel-archetype-spring (Creates a new Camel project with added Spring DSL support.)
21: remote -> org.apache.camel.archetypes:camel-archetype-spring-dm (Creates a new Camel project with added Spring DSL support. Ready to be deployed in OSGi.)
22: remote -> org.appfuse:appfuse-basic-spring (Maven 2 archetype that creates a web application with AppFuse embedded in it.)
23: remote -> org.appfuse:appfuse-modular-spring (Maven 2 archetype that creates a modular web application with AppFuse. This archetype creates two modules:
        "core" and "web". The core module depends on appfuse-service, while the web module depends on core as well
        as AppFuse's Spring MVC implementation.)
24: remote -> org.appfuse.archetypes:appfuse-basic-spring (Maven 2 archetype that creates a web application with AppFuse embedded in it.)
25: remote -> org.appfuse.archetypes:appfuse-basic-spring-archetype (AppFuse Archetype)
26: remote -> org.appfuse.archetypes:appfuse-light-spring-archetype (AppFuse Archetype)
27: remote -> org.appfuse.archetypes:appfuse-light-spring-freemarker-archetype (AppFuse Archetype)
28: remote -> org.appfuse.archetypes:appfuse-light-spring-security-archetype (AppFuse Archetype)
29: remote -> org.appfuse.archetypes:appfuse-modular-spring (Maven 2 archetype that creates a modular web application with AppFuse. This archetype creates two m
odules:
        "core" and "web". The core module depends on appfuse-service, while the web module depends on core as well
        as AppFuse's Spring MVC implementation.)
30: remote -> org.appfuse.archetypes:appfuse-modular-spring-archetype (AppFuse Archetype)
31: remote -> org.cometd.archetypes:cometd-archetype-spring-dojo-jetty7 (-)
32: remote -> org.cometd.archetypes:cometd-archetype-spring-dojo-jetty9 (-)
33: remote -> org.cometd.archetypes:cometd-archetype-spring-jquery-jetty7 (-)
34: remote -> org.cometd.archetypes:cometd-archetype-spring-jquery-jetty9 (-)
35: remote -> org.fluttercode.knappsack:spring-jsf-jpa-archetype (-)
36: remote -> org.fluttercode.knappsack:spring-mvc-jpa-archetype (-)
37: remote -> org.fluttercode.knappsack:spring-mvc-jpa-demo-archetype (-)
38: remote -> org.graniteds.archetypes:graniteds-flex-spring-jpa-hibernate (Base project with Flex 4.6, Spring 3 and Hibernate using GraniteDS with RemoteObject
 API.)
39: remote -> org.graniteds.archetypes:graniteds-spring-jpa-hibernate (Base project with Flex 4.5, Spring 3 and Hibernate using GraniteDS with RemoteObject API.
)
40: remote -> org.graniteds.archetypes:graniteds-tide-flex-spring-jpa-hibernate (Base project with Flex 4.6, Spring 3.1 and Hibernate 3.6 using GraniteDS with t
he Tide API.)
41: remote -> org.graniteds.archetypes:graniteds-tide-javafx-spring-jpa-hibernate (Base project with JavaFX 2.2, Spring 3.1 and Hibernate 3.6 using GraniteDS wi
th the Tide API.)
42: remote -> org.graniteds.archetypes:graniteds-tide-spring-jpa-hibernate (Base project with Flex 4.5, Spring 3 and Hibernate using GraniteDS with the Tide API
.)
43: remote -> org.jbehave:jbehave-spring-archetype (An archetype to run multiple textual stories configured programmatically but with steps classes composed usi
ng Spring.)
44: remote -> org.jbehave.web:jbehave-web-selenium-java-spring-archetype (An archetype to run web stories using Selenium, Java and Spring.)
45: remote -> org.jboss.archetype.wfk:jboss-spring-mvc-archetype (An archetype that generates a starter Spring MVC application with Java EE persistence settings
 (server bootstrapped JPA, JTA transaction management) for JBoss AS7)
46: remote -> org.jboss.spring.archetypes:jboss-spring-mvc-archetype (An archetype that generates a starter Spring MVC application with Java EE persistence sett
ings (server bootstrapped JPA, JTA transaction management) for JBoss AS7)
47: remote -> org.jboss.spring.archetypes:spring-mvc-webapp (An archetype that generates a starter Spring MVC application with Java EE persistence settings (ser
ver bootstrapped JPA, JTA transaction management) for JBoss AS7)
48: remote -> org.mixer2:mixer2-springmvc-archetype (archetype for SpringMVC web application with mixer2)
49: remote -> org.ops4j.pax.construct:maven-archetype-spring-bean (-)
50: remote -> org.springframework.boot:spring-boot-sample-actuator-archetype (Spring Boot Actuator Sample)
51: remote -> org.springframework.boot:spring-boot-sample-actuator-log4j-archetype (Spring Boot Actuator Log4J Sample)
52: remote -> org.springframework.boot:spring-boot-sample-actuator-noweb-archetype (Spring Boot Actuator Non-Web Sample)
53: remote -> org.springframework.boot:spring-boot-sample-actuator-ui-archetype (Spring Boot Actuator UI Sample)
54: remote -> org.springframework.boot:spring-boot-sample-amqp-archetype (Spring Boot AMQP Sample)
55: remote -> org.springframework.boot:spring-boot-sample-aop-archetype (Spring Boot AOP Sample)
56: remote -> org.springframework.boot:spring-boot-sample-batch-archetype (Spring Boot Batch Sample)
57: remote -> org.springframework.boot:spring-boot-sample-data-jpa-archetype (Spring Boot Data JPA Sample)
58: remote -> org.springframework.boot:spring-boot-sample-data-mongodb-archetype (Spring Boot Data MongoDB Sample)
59: remote -> org.springframework.boot:spring-boot-sample-data-redis-archetype (Spring Boot Data Redis Sample)
60: remote -> org.springframework.boot:spring-boot-sample-data-rest-archetype (Spring Boot Data REST Sample)
61: remote -> org.springframework.boot:spring-boot-sample-integration-archetype (Spring Boot Integration Sample)
62: remote -> org.springframework.boot:spring-boot-sample-jetty-archetype (Spring Boot Jetty Sample)
63: remote -> org.springframework.boot:spring-boot-sample-profile-archetype (Spring Boot Profile Sample)
64: remote -> org.springframework.boot:spring-boot-sample-secure-archetype (Spring Boot Security Sample)
65: remote -> org.springframework.boot:spring-boot-sample-servlet-archetype (Spring Boot Servlet Sample)
66: remote -> org.springframework.boot:spring-boot-sample-simple-archetype (Spring Boot Simple Sample)
67: remote -> org.springframework.boot:spring-boot-sample-tomcat-archetype (Spring Boot Tomcat Sample)
68: remote -> org.springframework.boot:spring-boot-sample-traditional-archetype (Spring Boot Traditional Sample)
69: remote -> org.springframework.boot:spring-boot-sample-web-jsp-archetype (Spring Boot Web JSP Sample)
70: remote -> org.springframework.boot:spring-boot-sample-web-method-security-archetype (Spring Boot Web Method Security Sample)
71: remote -> org.springframework.boot:spring-boot-sample-web-secure-archetype (Spring Boot Web Secure Sample)
72: remote -> org.springframework.boot:spring-boot-sample-web-static-archetype (Spring Boot Web Static Sample)
73: remote -> org.springframework.boot:spring-boot-sample-web-ui-archetype (Spring Boot Web UI Sample)
74: remote -> org.springframework.boot:spring-boot-sample-websocket-archetype (Spring Boot WebSocket Sample)
75: remote -> org.springframework.boot:spring-boot-sample-xml-archetype (Spring Boot XML Sample)
76: remote -> org.springframework.osgi:spring-osgi-bundle-archetype (Spring OSGi Maven2 Archetype)
77: remote -> org.springframework.ws:spring-ws-archetype (Spring Web Services Maven2 Archetype.)
78: remote -> org.sqlproc:sqlproc-archetype-simple-spring (SQL Processor Archetype for Simple Spring Application)
79: remote -> org.xaloon.archetype:xaloon-archetype-wicket-jpa-spring (-)
80: remote -> org.zkoss:zk-ee-eval-archetype-webapp-spring (An archetype that generates a starter ZK EE-eval webapp project with Spring)
81: remote -> org.zkoss:zk-ee-eval-archetype-webapp-spring-jpa (An archetype that generates a starter ZK EE-eval webapp project with Spring and JPA)
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains): :
```

我们选择47 "spring-mvc-webapp"

```sh
47: remote -> org.jboss.spring.archetypes:spring-mvc-webapp (An archetype that generates a starter Spring MVC application with Java EE persistence settings (ser
ver bootstrapped JPA, JTA transaction management) for JBoss AS7)
```

输入一系列的参数后，我们已经建好了一个项目```MySpringApp```，以下是输出内容：

```sh
8: 1.0.0.CR8
Choose a number: 8: 8
Downloading: http://repo.maven.apache.org/maven2/org/jboss/spring/archetypes/spring-mvc-webapp/1.0.0.CR8/spring-mvc-webapp-1.0.0.CR8.jar
Downloaded: http://repo.maven.apache.org/maven2/org/jboss/spring/archetypes/spring-mvc-webapp/1.0.0.CR8/spring-mvc-webapp-1.0.0.CR8.jar (93 KB at 32.6 KB/sec)
Downloading: http://repo.maven.apache.org/maven2/org/jboss/spring/archetypes/spring-mvc-webapp/1.0.0.CR8/spring-mvc-webapp-1.0.0.CR8.pom
Downloaded: http://repo.maven.apache.org/maven2/org/jboss/spring/archetypes/spring-mvc-webapp/1.0.0.CR8/spring-mvc-webapp-1.0.0.CR8.pom (4 KB at 2.9 KB/sec)
Define value for property 'groupId': : info.woodchat
Define value for property 'artifactId': : MySpringApp
Define value for property 'version':  1.0-SNAPSHOT: :
Define value for property 'package':  info.woodchat: :
[INFO] Using property: enterprise = false
[INFO] Using property: springBomVersion = 2.0.0-beta-6
Confirm properties configuration:
groupId: info.woodchat
artifactId: MySpringApp
version: 1.0-SNAPSHOT
package: info.woodchat
enterprise: false
springBomVersion: 2.0.0-beta-6
 Y: :
[INFO] ----------------------------------------------------------------------------
[INFO] Using following parameters for creating project from Archetype: spring-mvc-webapp:1.0.0.CR8
[INFO] ----------------------------------------------------------------------------
[INFO] Parameter: groupId, Value: info.woodchat
[INFO] Parameter: artifactId, Value: MySpringApp
[INFO] Parameter: version, Value: 1.0-SNAPSHOT
[INFO] Parameter: package, Value: info.woodchat
[INFO] Parameter: packageInPathFormat, Value: info/woodchat
[INFO] Parameter: package, Value: info.woodchat
[INFO] Parameter: version, Value: 1.0-SNAPSHOT
[INFO] Parameter: groupId, Value: info.woodchat
[INFO] Parameter: springBomVersion, Value: 2.0.0-beta-6
[INFO] Parameter: artifactId, Value: MySpringApp
[INFO] Parameter: enterprise, Value: false
[INFO] project created from Archetype in dir: e:\kbase\java\maven\example\MySpringApp
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 4:37.097s
[INFO] Finished at: Thu Sep 04 16:37:02 CST 2014
[INFO] Final Memory: 9M/32M
[INFO] ------------------------------------------------------------------------
```

###2.pom.xml###

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>info.woodchat</groupId>
    <artifactId>MySpringApp</artifactId>
    <packaging>war</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>Getting Started with Spring on JBoss</name>
    <properties>
        <version.jboss.bom>1.0.5.Final</version.jboss.bom>
        <version.standard.taglibs>1.1.2</version.standard.taglibs>
        <version.commons.logging>1.1.1</version.commons.logging>
        <version.jboss.as.maven.plugin>7.3.Final</version.jboss.as.maven.plugin>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.jboss.bom</groupId>
                <artifactId>jboss-javaee-6.0-with-hibernate</artifactId>
                <version>${version.jboss.bom}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            
             <dependency>
                <groupId>org.jboss.bom</groupId>
                <artifactId>jboss-javaee-6.0-with-spring</artifactId>
                <version>${version.jboss.bom}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            
            <dependency>
                <groupId>taglibs</groupId>
                <artifactId>standard</artifactId>
                <version>${version.standard.taglibs}</version>
            </dependency>

            <dependency>
                <groupId>commons-logging</groupId>
                <artifactId>commons-logging</artifactId>
                <version>${version.commons.logging}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>org.hibernate.javax.persistence</groupId>
            <artifactId>hibernate-jpa-2.0-api</artifactId>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-validator</artifactId>
            <scope>provided</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-api</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-entitymanager</artifactId>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-validator-annotation-processor</artifactId>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-orm</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-tx</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
        </dependency>

        <dependency>
            <groupId>aopalliance</groupId>
            <artifactId>aopalliance</artifactId>
        </dependency>
        <dependency>
            <groupId>taglibs</groupId>
            <artifactId>standard</artifactId>
        </dependency>
        <dependency>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </dependency>

        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.8.2</version>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>cglib</groupId>
            <artifactId>cglib-nodep</artifactId>
            <version>2.2</version>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <version>1.3.165</version>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.codehaus.jackson</groupId>
            <artifactId>jackson-mapper-asl</artifactId>
            <version>1.9.3</version>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.codehaus.jackson</groupId>
            <artifactId>jackson-core-asl</artifactId>
            <version>1.9.3</version>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>1.6.4</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <finalName>MySpringApp</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>2.4</version>
                <configuration>
                    <source>1.6</source>
                    <target>1.6</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.jboss.as.plugins</groupId>
                <artifactId>jboss-as-maven-plugin</artifactId>
                <version>${version.jboss.as.maven.plugin}</version>
            </plugin>
            <plugin>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>2.12</version>
            </plugin>
        </plugins>
    </build>
    <profiles>
        <profile>
            <id>openshift</id>
            <build>
                <plugins>
                    <plugin>
                        <artifactId>maven-war-plugin</artifactId>
                        <version>2.2</version>
                        <configuration>
                            <outputDirectory>deployments</outputDirectory>
                            <warName>ROOT</warName>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>
</project>
```


##如何转换Java web项目到基于Maven的项目##

Maven没有完全提供解决方案转换一个已经存在的Java web项目到一个基于Maven的web项目，基本上，基于Maven的项目主要有2个主要的变化，它们是：
1. 文件夹结构 - 参考[官方文档](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)；
2. 依赖包 - 把所有的依赖包放在你的```pom.xml```文件中。

###转换Java项目到Maven项目的步骤###

####1. Maven web项目目录结构####
  1. 把已存在的java pakcage和.java文件移到 - "```\src\main\java```"文件夹中；
  2. 把"web.xml"文件移到 - "```\src\main\webapp\WEB-INF```"文件夹中；
  3. 新建一个"pom.xml"文件，并把它放在根目录中。

####2. 项目细节####
  在根目录新建或配置已有的```pom.xml```文件，添加远程仓库，war插件和编译插件
####3. 配置依赖包####
  你需要手动添加项目需要的依赖包到"```pom.xml```"文件中，在[Maven Centeral Repository](http://repo1.maven.org/maven2)和[Java.net Maven Repository](http://download.java.net/maven/2)中查找你需要的依赖库。
####4. 编译 - "mvn compile"####
```sh
E:\workspace\servletdemo\mvn compile
.......
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
```

####5. 让它支持Eclipse
```sh
mvn eclipse:eclipse -Dwtpversion=2.0
```

####6. 生成部署包war文件####
```sh
E:\workspace\serlvetdemo>mvn war:war
[INFO] Scanning for projects...
.......
[INFO] Processing war project
[INFO] Copying webapp resources[E:\workspace\serlvetde
[INFO] Webapp assembled in[47 msecs]
[INFO] Building war: E:\workspace\serlvetdemo\target\s
[INFO] -----------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] -----------------------------------------------
...

```

####7. 完成####


##如何使用Maven构建项目##
想要构建一个基于Maven的项目，你需要在终端或者命令提示符进入到```pom.xml```文件所在目录，输入命令：
```sh
mvn package
```
> 当执行"```mvn package```"时，需要经过以下阶段 - "validate","compile"和"test"，最好一步是"package"

####"mvn package"样例####
当你运行"```mvn package```"命令，它将会依据```pom.xml```文件中"packaging"标记编译源码，运行单元测试类最后打包。举个例子，
  1. 如果"packaging"=jar,它将会打包你的项目到一个"jar"文件并放到target文件夹
  ```xml
    <modelVersion>4.0.0</modelVersion>
    <groupId>info.woodchat</groupId>
    <artifactId>Maven Example</artifactId>
    <packaging>jar</packaging>
  ```

  2. 如果"packaging"=war，它将会打包你的项目到一个"war"文件并放到target文件夹
  ```xml
    <modelVersion>4.0.0</modelVersion>
    <groupId>info.woodchat</groupId>
    <artifactId>Maven Example</artifactId>
    <packaging>war</packaging>
  ```

##如何使用Maven清理项目##
在基于Maven的项目中，很多缓存输出到你的"target"文件夹中，当你需要构建一个项目去部署时，你必须保证清理所有缓存的输出，你才能得到最新的部署包。

想要清理你的项目缓存输出，输入这个命令：
```sh
mvn clean
```
输出：
```sh
D:\workspace-new>mvn clean
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Building test Maven Webapp
[INFO]    task-segment: [clean]
[INFO] ------------------------------------------------------------------------
[INFO] [clean:clean {execution: default-clean}]
[INFO] Deleting directory D:\workspace-new\test\target
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1 second
[INFO] Finished at: Fri Apr 15 16:42:58 SGT 2011
[INFO] Final Memory: 3M/6M
[INFO] ------------------------------------------------------------------------
```

当"mvn clean"执行完后，"**target**"文件夹所有的内容都会被删除。

> 想要部署你的项目到生产系统，总是建议执行"```mvn clean package```"来确保得到最新的部署包。


##如何使用Maven运行单元测试##
```sh
mvn test
```
将会运行项目所有的单元测试类。

###案例学习###
新建2个unit case，下面是Java类
```java
package info.woodchat.core; 
public class App {
  public static void main(String[] args) { 
    System.out.println(getHelloWorld()); 
  } 
  public static String getHelloWorld() { 
    return "Hello World"; 
  } 
  public static String getHelloWorld2() { 
    return "Hello World 2"; 
  }
}
```

####Unit Test 1####

```java
package info.woodchat.core.test; 
import junit.framework.Assert;
import org.junit.Test; 
public class TestApp1 { 
  @Test
  public void testPrintHelloWorld() { 
    Assert.assertEquals(App.getHelloWorld(), "Hello World"); 
  } 
}

```

####Unit Test 2####
```java
package info.woodchat.core; 
import junit.framework.Assert;
import org.junit.Test; 
public class TestApp2 { 
  @Test
  public void testPrintHelloWorld2() { 
    Assert.assertEquals(App.getHelloWorld2(), "Hello World 2"); 
  } 
}
```

####Run Unit Test####
1. 运行所有unit test(TestApp1和TestApp)
```sh
mvn test
```

2.运行TestApp1的unit test
```sh
mvn -Dtest=TestApp1 test
```

3.运行TestApp2的unit test
```sh
mvn -Dtest=TestApp2 test
```


##如何安装你的项目到本地Maven库##
在Maven中，你可以使用```mvn install```来打包你的项目并且部署到你的本地仓库中，这样其它开发人员可以使用。
```sh
mvn install
```

###mvn install样例###
一个Java项目，有一个```pom.xml```文件
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>info.woodchat.core</groupId>
  <artifactId>woodchat-core</artifactId>
  <packaging>jar</packaging>
  <version>99</version>
  <name>woodchat-core</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.4</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

根据上面的```pom.xml```文件，当执行玩```mvn instal```，将会自动打包到"```woodchat-core-99.jar"文件并且复制到你本地仓库。

> 建议：一起运行"**clean**"和"**install**"，这样总会部署一个最新的项目到本地仓库

```sh
mvn clean install
```

###访问你部署的项目###
现在，其它开发人员将能访问你部署的“jar”通过在```pom.xml```文件中申明下面的依赖
```xml
<dependency>
    <groupId>info.woodchat.core</groupId>
    <artifactId>woodchat-core</artifactId>
    <version>99</version>
 </dependency>
```


##如何为基于Maven的项目生成一个文档站点##
在Maven中，你可以使用下面的命令为你的项目生成一个文档站点
```sh
mvn site
```

生成的文档将会存放在"**target/site**"文件夹中


##如何部署基于Maven的项目到Tomcat中##
在这一节中，我们讲演示如何使用[Maven-Tomcat plugin](http://tomcat.apache.org/maven-plugin.html)来打包并且部署一个WAR文件到Tomcat中。Tomcat6 和 Tomcat7

###1. Tomcat 7 例子###
这个例子演示如何打包部署一个WAR文件到Tomcat7
####1.1 Tomcat Authentication####
添加一个用户角色```manager-gui```和```manager-script```
```xml
<!--%TOMCAT7_PATH%/conf/tomcat-users.xml-->
<?xml version='1.0' encoding='utf-8'?>
<tomcat-users> 
  <role rolename="manager-gui"/>
  <role rolename="manager-script"/>
  <user username="admin" password="password" roles="manager-gui,manager-script" /> 
</tomcat-users>
```

####1.2 Maven Authentication####
添加上面的Tomcat用户到Maven settings文件，这样Maven可以使用这个用户登录Tomcat server
```xml
<!--%MAVEN_PATH%/conf/settings.xml-->
<?xml version="1.0" encoding="UTF-8"?>
<settings ...>
  <servers> 
    <server>
      <id>TomcatServer</id>
      <username>admin</username>
      <password>password</password>
    </server> 
  </servers>
</settings>
```

####1.3 添加Tomcat7 Maven Plugin到```pom.xml```文件####
定义一个Maven Tomcat plugin
```xml
  <!--pom.xml-->
  <plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.2</version>
    <configuration>
      <url>http://localhost:8080/manager/text</url>
      <server>TomcatServer</server>
      <path>/woodchatWebApp</path>
    </configuration>
  </plugin>
```

在部署过程中，它告诉Maven通过"http://localhost:8080/manager/text"部署一个WAR文件到Tomcat server，访问路径为"/woodchatWebApp", 使用"TomcatServer"(在settings.xml) 

####1.4 部署到Tomcat####
```sh
mvn tomcat7:deploy
mvn tomcat7:undeploy
mvn tomcat7:redeploy
```
例子
```sh
> mvn tomcat7:deploy 
...
[INFO] Deploying war to http://localhost:8080/woodchatWebApp
Uploading: http://localhost:8080/manager/text/deploy?path=%2FwoodchatWebApp&update=true
Uploaded: http://localhost:8080/manager/text/deploy?path=%2FwoodchatWebApp&update=true (13925 KB at 35250.9 KB/sec)
 
[INFO] tomcatManager status code:200, ReasonPhrase:OK
[INFO] OK - Deployed application at context path /woodchatWebApp
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 8.507 s
[INFO] Finished at: 2014-08-05T11:35:25+08:00
[INFO] Final Memory: 28M/308M
[INFO] ------------------------------------------------------------------------
```

###2. Tomcat 6 例子###
这个例子演示如何打包部署一个WAR文件到Tomcat 6。步骤和Tomcat 7一样，只是部署的url和命令不同
####2.1Tomcat Authentication
```
<!--%TOMCAT6_PATH%/conf/tomcat-users.xml-->
<?xml version='1.0' encoding='utf-8'?>
<tomcat-users> 
  <role rolename="manager-gui"/>
  <role rolename="manager-script"/>
  <user username="admin" password="password" roles="manager-gui,manager-script" /> 
</tomcat-users>
```

####2.2Maven Authentication####
```xml
<!--%MAVEN_PATH%/conf/settings.xml-->
<?xml version="1.0" encoding="UTF-8"?>
<settings ...>
  <servers> 
    <server>
      <id>TomcatServer</id>
      <username>admin</username>
      <password>password</password>
    </server> 
  </servers>
</settings>
```

####2.3Tomcat6 Maven Plugin####
```xml
  <!--pom.xml-->
  <plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat6-maven-plugin</artifactId>
    <version>2.2</version>
    <configuration>
      <url>http://localhost:8080/manager</url>
      <server>TomcatServer</server>
      <path>/woodchatWebApp</path>
    </configuration>
  </plugin>
```

####2.4部署到Tomcat 6####
mvn tomcat6:deploy 
mvn tomcat6:undeploy 
mvn tomcat6:redeploy
```

例子
```sh
> mvn tomcat6:deploy
...
[INFO] Deploying war to http://localhost:8080/woodchatWebApp
Uploading: http://localhost:8080/manager/deploy?path=%2FwoodchatWebApp
Uploaded: http://localhost:8080/manager/deploy?path=%2FwoodchatWebApp (13925 KB at 32995.5 KB/sec)
 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 22.652 s
[INFO] Finished at: 2014-08-05T12:18:54+08:00
[INFO] Final Memory: 30M/308M
[INFO] ------------------------------------------------------------------------
```

