package info.woodchat.javaconfig;

import info.woodchat.core.Hello;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//ApplicationContext context = new ClassPathXmlApplicationContext("SpringBeans.xml");
		ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
	    IHelloWorld obj = (IHelloWorld) context.getBean("helloBean");	    
	    obj.printHelloWorld("Spring3 Java Config");
	}

}
