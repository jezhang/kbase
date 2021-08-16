"use strict";
// 2.1 Boolean 类型
var isDone = false;
console.log("isDone: " + isDone);
// 2.2 Number 类型
var count = 10;
console.log("count: " + count);
// String 类型
var myName = "Semliker";
console.log("myName: " + myName);
// 2.4 Array 类型
var stringList = ["a", "b", "c"];
console.log("stringList: " + stringList);
var numberList = [4, 5, 6];
console.log("numberList: " + numberList);
// 2.5 Enum 类型
// 1.数字枚举
var Direction;
(function (Direction) {
    Direction[Direction["NORTH"] = 0] = "NORTH";
    Direction[Direction["SOUTH"] = 1] = "SOUTH";
    Direction[Direction["EAST"] = 2] = "EAST";
    Direction[Direction["WEST"] = 3] = "WEST";
})(Direction || (Direction = {}));
var dir = Direction.SOUTH;
console.log("dir: " + dir);
// 2.字符串枚举
var DIR;
(function (DIR) {
    DIR["NORTH"] = "NORTH";
    DIR["SOUTH"] = "SOUTH";
    DIR["EAST"] = "EAST";
    DIR["WEST"] = "WEST";
})(DIR || (DIR = {}));
var dir2 = DIR.WEST;
console.log("dir2: " + dir2);
// 3.异构枚举
var Enum;
(function (Enum) {
    Enum[Enum["A"] = 0] = "A";
    Enum[Enum["B"] = 1] = "B";
    Enum["C"] = "C";
    Enum["D"] = "D";
    Enum[Enum["E"] = 8] = "E";
    Enum[Enum["F"] = 9] = "F";
})(Enum || (Enum = {}));
console.log("Enum.A: " + Enum.A); //输出：0
console.log("Enum[0]: " + Enum[0]); // 输出：A
// 2.6 Any 类型
// 在 TypeScript 中，任何类型都可以被归为 any 类型。这让 any 类型成为了类型系统的顶级类型（也被称作全局超级类型）。
var notSure = 666;
console.log("notSure: " + notSure);
notSure = "Semlinker";
console.log("notSure: " + notSure);
notSure = false;
console.log("notSure: " + notSure);
/*
在许多场景下，这太宽松了。使用 any 类型，可以很容易地编写类型正确但在运行时有问题的代码。
如果我们使用 any 类型，就无法使用 TypeScript 提供的大量的保护机制。为了解决 any 带来的问题，
TypeScript 3.0 引入了 unknown 类型。
*/
// 2.7 Unknown 类型
/*
就像所有类型都可以赋值给 any，所有类型也都可以赋值给 unknown。这使得 unknown 成为 TypeScript 类型系统的另一种顶级类型（另一种是 any）。
下面我们来看一下 unknown 类型的使用示例：
*/
var value;
value = true; // OK
value = 42; // OK
value = "Hello World"; // OK
value = []; // OK
value = {}; // OK
value = Math.random; // OK
value = null; // OK
value = undefined; // OK
value = new TypeError(); // OK
// value = Symbol("type"); // OK
/*
对 value 变量的所有赋值都被认为是类型正确的。但是，当我们尝试将类型为 unknown 的值赋值给其他类型的变量时会发生什么？
*/
/*
let value: unknown;

let value1: unknown = value; // OK
let value2: any = value; // OK
let value3: boolean = value; // Error
let value4: number = value; // Error
let value5: string = value; // Error
let value6: object = value; // Error
let value7: any[] = value; // Error
let value8: Function = value; // Error
*/
/*
unknown 类型只能被赋值给 any 类型和 unknown 类型本身。
直观地说，这是有道理的：只有能够保存任意类型值的容器才能保存 unknown 类型的值。
毕竟我们不知道变量 value 中存储了什么类型的值。
*/
// 2.8 Tuple 类型
/*
众所周知，数组一般由同种类型的值组成，但有时我们需要在单个变量中存储不同类型的值，这时候我们就可以使用元组。
在 JavaScript 中是没有元组的，元组是 TypeScript 中特有的类型，其工作方式类似于数组。
*/
/*
元组可用于定义具有有限数量的未命名属性的类型。每个属性都有一个关联的类型。
使用元组时，必须提供每个属性的值。为了更直观地理解元组的概念，我们来看一个具体的例子：
*/
var tupleType;
tupleType = ["Semlinker", true];
/*
在上面代码中，我们定义了一个名为 tupleType 的变量，它的类型是一个类型数组 [string, boolean]，
然后我们按照正确的类型依次初始化 tupleType 变量。与数组一样，我们可以通过下标来访问元组中的元素：
*/
console.log("tupleType[0]: " + tupleType[0]); // Semlinker
console.log("tupleType[1]: " + tupleType[1]); // true
// 2.9 Void 类型
/*
某种程度上来说，void 类型像是与 any 类型相反，它表示没有任何类型。当一个函数没有返回值时，你通常会见到其返回值类型是 void：
*/
// 声明函数返回值为void
function warnUser() {
    console.log("This is my warning message");
}
warnUser();
/*需要注意的是，声明一个 void 类型的变量没有什么作用，因为它的值只能为 undefined 或 null：*/
var unusable = undefined;
// 2.10 Null 和 Undefined 类型
/* TypeScript 里，undefined 和 null 两者有各自的类型分别为 undefined 和 null。*/
var u = undefined;
var n = null;
/*
默认情况下 null 和 undefined 是所有类型的子类型。 就是说你可以把 null 和 undefined 赋值给 number 类型的变量。
然而，如果你指定了--strictNullChecks 标记，null 和 undefined 只能赋值给 void 和它们各自的类型。
*/
// 2.11 Never 类型
/*
never 类型表示的是那些永不存在的值的类型。 例如，never 类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型。
*/
// 返回never的函数必须存在无法达到的终点
function error(message) {
    throw new Error(message);
}
function infiniteLoop() {
    while (true) { }
}
// type Foo = string | number | boolean;
function controlFlowAnalysisWithNever(foo) {
    if (typeof foo === "string") {
        // 这里 foo 被收窄为 string 类型
    }
    else if (typeof foo === "number") {
        // 这里 foo 被收窄为 number 类型
    }
    else {
        // foo 在这里是 never
        var check = foo;
    }
}
/*
注意在 else 分支里面，我们把收窄为 never 的 foo 赋值给一个显示声明的 never 变量。
如果一切逻辑正确，那么这里应该能够编译通过。但是假如后来有一天你的同事修改了 Foo 的类型：
*/
// type Foo = string | number | boolean;
/*
然而他忘记同时修改 controlFlowAnalysisWithNever 方法中的控制流程，
这时候 else 分支的 foo 类型会被收窄为 boolean 类型，导致无法赋值给 never 类型，
这时就会产生一个编译错误。通过这个方式，我们可以确保
*/
/*
controlFlowAnalysisWithNever 方法总是穷尽了 Foo 的所有可能类型。
通过这个示例，我们可以得出一个结论：使用 never 避免出现新增了联合类型没有对应的实现，目的就是写出类型绝对安全的代码。
*/ 
