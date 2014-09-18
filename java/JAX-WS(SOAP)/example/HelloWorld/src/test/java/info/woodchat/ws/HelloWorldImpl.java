package info.woodchat.ws;

import javax.jws.WebService;

@WebService(endpointInterface = "info.woodchat.ws.HelloWorld")
public class HelloWorldImpl implements HelloWorld {
	@Override
	public String getHelloWorldAsString(String name) {
		return "Hello World JAX-WS " + name;
	}
}
