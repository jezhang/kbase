package info.woodchat.core;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App 
{
    public static void main( String[] args )
    {
//        System.out.println( "Hello World!" );
    	ApplicationContext context = new ClassPathXmlApplicationContext("SpringBeans.xml");
    	Hello obj = (Hello) context.getBean("helloBean");
    	obj.printHello();    	
    }
}
