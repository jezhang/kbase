console.log(`Hello World!`);


let someValue1: any = "this is a string";
let strLength1: number = (<string>someValue1).length;


let someValue2: any = "this is a string";
let strLength2: number = (someValue2 as string).length;