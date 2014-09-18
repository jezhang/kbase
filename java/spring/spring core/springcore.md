Spring教程
==========

##Spring快速开始##

###Spring hello world 例子###
这个例子我们使用Maven创建一个简单的Java项目结构，并演示如何获取Spring bean来打印"hello world"字符串。
####1.使用Maven创建项目目录####
```sh
mvn archetype:generate -DgroupId=info.woodchat.common -DartifactId=SpringExamples -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

####2.转换成Eclipse项目####
```sh
mvn eclipse:eclipse
```

> 手动创建一个"**resources**"文件夹"，路径为：**/src/main/resources**"，用来存放Spring bean xml配置文件。Maven会将所有"resources"文件下的所有文件看作资源文件，并自动复制到classes文件夹

####3.添加Spring依赖到pom.xml中####
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
	http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>info.woodchat.common</groupId>
	<artifactId>SpringExamples</artifactId>
	<packaging>jar</packaging>
	<version>1.0-SNAPSHOT</version>
	<name>SpringExamples</name>
	<url>http://maven.apache.org</url>
	<dependencies> 
		<!-- Spring framework -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring</artifactId>
			<version>2.5.6</version>
		</dependency> 
	</dependencies>
</project>
```

再次执行"**mvn eclipse:eclipse**"，Maven将会自动下载Spring依赖包并且放到Maven本地仓库中。同时，Maven也会把下载好的包添加到"**.classpath**"文件中。

####4.Spring bean(Java class)####
在目录“/src/main/java/info/woodchat/common/HelloWorld.java”新建一个Java类文件(HelloWorld.java)
```java
package info.woodchat.common;
public class HelloWorld {
	private String name; 
	public void setName(String name) {
		this.name = name;
	} 
	public void printHello() {
		System.out.println("Hello ! " + name);
	}
}
```
####5.Spring bean配置文件####
新建“/src/main/resources/Spring-Module.xml”。这是一个Spring bean配置文件
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-2.5.xsd"> 
	<bean id="helloBean" class="info.woodchat.common.HelloWorld">
		<property name="name" value="Mkyong" />
	</bean> 
</beans>
```
####6.运行####
运行```App.java```，它将加载Spring bean配置文件(**Spring-Module.xml**)并且通过```getBean()```方法获取到Spring bean
```java
// App.java
package info.woodchat.common; 
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
 
public class App {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext(
				"Spring-Module.xml"); 
		HelloWorld obj = (HelloWorld) context.getBean("helloBean");
		obj.printHello();
	}
}
```


###Spring 3.0 hello world 例子###
Spring 3.0最低需要JDK1.5支持
> 在Spring 2.5.x中，几乎所有的Spring模块都放进一个单独的spring.jar文件中，从Spring 3.0开始，每个模块分离成一个个独立的jar文件，例如： spring-core, spring-expression, spring-context, spring-aop等。 更多详细信息请参考[官方文档](http://blog.springsource.com/2009/12/02/obtaining-spring-3-artifacts-with-maven/)

####1.使用Maven创建文件结构####
```sh
mvn archetype:generate -DgroupId=info.woodchat.core -DartifactId=Spring3Example -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

####2.转换成Eclipse项目####
```sh
mvn eclipse:eclipse
```

####3.添加Spring 3.0依赖到pom.xml####
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
	http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>info.woodchat.core</groupId>
	<artifactId>Spring3Example</artifactId>
	<packaging>jar</packaging>
	<version>1.0-SNAPSHOT</version>
	<name>Spring3Example</name>
	<url>http://maven.apache.org</url> 
	<properties>
		<spring.version>3.0.5.RELEASE</spring.version>
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
			<artifactId>spring-context</artifactId>
			<version>${spring.version}</version>
		</dependency> 
	</dependencies>
</project>
```

####4.Spring bean####
```java
package info.woodchat.core;
public class HelloWorld {
	private String name; 
	public void setName(String name) {
		this.name = name;
	} 
	public void printHello() {
		System.out.println("Spring 3 : Hello ! " + name);
	}
}
```

####5.Spring bean配置文件####
新建“/src/main/resources/SpringBeans.xml”。这是一个Spring bean配置文件
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-3.0.xsd"> 
	<bean id="helloBean" class="info.woodchat.core.HelloWorld">
		<property name="name" value="Jean Zhang" />
	</bean> 
</beans>
```

####6.运行####
运行```App.java```，它将加载Spring bean配置文件(**SpringBeans.xml**)并且通过```getBean()```方法获取到Spring bean
```java
// App.java
package info.woodchat.core; 
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext; 
public class App {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext(
				"SpringBeans.xml"); 
		HelloWorld obj = (HelloWorld) context.getBean("helloBean");
		obj.printHello();
	}
}
```


###Spring 松耦合例子###

##Spring JavaConfig(Spring 3.0)##

##Spring依赖注入(DI)##

##Bean Basic##

##Spring表达式语言(Spring 3.0)##

##Spring自动组件扫描##

##Spring AutoWiring Bean##

##Spring AOP(面向方面编程)##

##Spring JDBC 支持##

##Spring Hibernate 支持##

##Spring E-mail 支持##

##Spring Scheduling 支持##

##Spring与其它框架的集成##

##Spring 常见问题##

##Spring 常见错误##

##Spring 参考##