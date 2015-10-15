package info.woodchat.ws.document;

import javax.jws.WebService;

@WebService(endpointInterface="info.woodchat.ws.document.HelloWorld")
public class HelloWorldImpl implements HelloWorld {
	@Override
	public String getHelloWorldAsString(String name) {
		return "Hello World JAX-WS " + name;
	}

}
