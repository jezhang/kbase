package info.woodchat.core;

public class Hello {
	private String name;
	public void setName(String name) {
		this.name = name;
	}
	
	public void printHello() {
		System.out.println("Spring 3 : Hello ! " + name);
	}
}
