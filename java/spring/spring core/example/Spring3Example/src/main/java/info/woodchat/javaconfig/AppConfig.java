package info.woodchat.javaconfig;

import info.woodchat.core.Hello;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {
	
	@Bean(name="helloBean")
	public IHelloWorld helloWorld() {
		return new HelloWorldImpl();
	}
}
