package info.woodchat.javaconfig;

public class HelloWorldImpl implements IHelloWorld {
	@Override
	public void printHelloWorld(String msg) {
		System.out.println("Hello : " + msg);
	}
}
