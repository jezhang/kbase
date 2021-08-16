const sayHello = (name:string | undefined | null) => {
  console.log(`Hello ${name}`);
}

sayHello("Semlinker");
sayHello(undefined);
sayHello(null)