
了不起的 TypeScript 入门教程
========================


![](https://segmentfault.com/img/bVbH9l1)


## 一、TypeScript 是什么

TypeScript 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集，而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。

TypeScript 提供最新的和不断发展的 JavaScript 特性，包括那些来自 2015 年的 ECMAScript 和未来的提案中的特性，比如异步功能和 Decorators，以帮助建立健壮的组件。下图显示了 TypeScript 与 ES5、ES2015 和 ES2016 之间的关系：

![](https://segmentfault.com/img/bVbH9l8)

### 1.1 TypeScript 与 JavaScript 的区别

![](https://gitee.com/ztmtim/picbed/raw/master/img/20210812170827.png)

### 1.2 获取TypeScript

命令行的 TypeScript 编译器可以使用 Node.js 包来安装。

#### 1.安装TypeScript

```sh
$ npm install -g typescript
```

#### 2.编译 TypeScript 文件

```sh
$ tsc -v
$ tsc helloworld.ts
# helloworld.ts => helloworld.js
```

## 二、TypeScript 基础类型

> 请阅读chap02.ts

## 三、TypeScript 断言


有时候你会遇到这样的情况，你会比 TypeScript 更了解某个值的详细信息。通常这会发生在你清楚地知道一个实体具有比它现有类型更确切的类型。


通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。类型断言好比其他语言里的类型转换，但是不进行特殊的数据检查和解构。它没有运行时的影响，只是在编译阶段起作用。


类型断言有两种形式：

### 3.1 “尖括号” 语法

```ts
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
```

### 3.2 as 语法

```ts
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;
```

> 请阅读chap03.ts


## 四、类型守卫

> A type guard is some expression that performs a runtime check that guarantees the type in some scope. —— TypeScript 官方文档

类型保护是可执行运行时检查的一种表达式，用于确保该类型在一定的范围内。换句话说，类型保护可以保证一个字符串是一个字符串，尽管它的值也可以是一个数值。类型保护与特性检测并不是完全不同，其主要思想是尝试检测属性、方法或原型，以确定如何处理值。目前主要有四种的方式来实现类型保护：

### 4.1 in 关键字

### 4.2 typeof 关键字

typeof 类型保护只支持两种形式：typeof v === "typename" 和 typeof v !== typename，"typename" 必须是 "number"， "string"， "boolean" 或 "symbol"。 但是 TypeScript 并不会阻止你与其它字符串比较，语言不会把那些表达式识别为类型保护。

### 4.3 instanceof 关键字

### 4.4 自定义类型保护的类型谓词


## 五、联合类型和类型别名

### 5.1 联合类型

联合类型通常与 null 或 undefined 一起使用：

```ts
const sayHello = (name: string | undefined) => {
  /* ... */
};
```

例如，这里 name 的类型是 string | undefined 意味着可以将 string 或 undefined 的值传递给sayHello 函数。

```ts
sayHello("Semlinker");
sayHello(undefined);
```
通过这个示例，你可以凭直觉知道类型 A 和类型 B 联合后的类型是同时接受 A 和 B 值的类型。




## References

<https://segmentfault.com/a/1190000022876390>