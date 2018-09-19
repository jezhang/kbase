
再举几个动态语言 eval 手法的例子
==============================

## 动态语言

假设要你实现一个函数，用来完成两个数的“某种运算”，具体的运算类型作为函数的参数传入，然后该函数返回运算结果。比如：

```py
foo("+", 2, 4)　# 返回 6
foo("*", 3, 5)　# 返回 15
```

　　如果你用静态语言（比如 C、C++、Java）来实现，你可能会在函数内使用一个 switch，根据不同的运算符，进行计算，然后返回计算结果。 　　

　　对于某些比较 ＯＯ 的语言（例如 C++、Java），你或许还会抽象出一个运算的接口类（纯虚类），然后分别派生出若干个不同的计算类（比如加法类、乘法类），看起来似乎比 switch 要优雅一些。

 　　当然，用静态语言还有其它一些玩法，但是代码量都不会少。具体详情可以看很早以前的一个老故事：《[4个程序员的一天](http://www.cnblogs.com/linkcd/archive/2005/07/19/196087.html)》。（其实俺这个例子的灵感就是从那个老故事剽窃滴） 　　现在，咱们来看看 Python 是如何【优雅地】实现该需求滴。用 Python 只需要【两行代码】即可。请看：

```py
def Foo(op, n1, n2) :
    return eval( "%d %s %d" % (n1, op, n2) )
```

　　不懂 Python 的同学可能要问了，这两行代码是啥子意思呀？

　　其实，第一行代码只不过是定义了一个函数头，第2行代码才是精华。这里面利用了动态语言常见的 **eval** 手法（具体参见“[这里](https://en.wikipedia.org/wiki/Eval)”）。在 python 里面，内置的 **eval** 函数可以把某个字符串当成一个表达式，并对其求值。而语句 "%d %s %d" % (n1, op, n2) 只不过格式化出一个表达式的字符串。

　　顺便再插一句，Python 还有一个 **exec** 的内置函数，可以把一段 Python 源代码作为字符串参数传递给它，让该函数去执行。两个函数结合起来，就能玩出很多花样。

## 示例１

先稍微扩展一下之前的例子，把两个数的某种运算扩展为多个数的某种运算。也就是说，给定某种运算类型（比如 

\*表示乘法、+ 表示加法）以及若干个数，要求返回运算结果。
举例：

给定："+" 和 4、5、6，返回 15。

给定："\*" 和 2、3、4、5，返回 120。

对于诸如 C/C++/Java 等非动态的语言，多半得定义具有两参数的函数：其中一个参数表示运算类型，另一个参数表示数组。至于函数实现，基本上还是那几招。要么通过 switch 来搞定——面向过程的路子；要么抽象出一个用于运算的接口类（纯虚类），然后针对每一种操作符去派生出不同的实现（比如加法类、乘法类）——也就是面向对象的路子。当然，想卖弄 C/C++ 宏技巧的同学，或许也能用宏函数搞定，但代码会比原先复杂得多。

现在，咱们来看看 Python 的 eval 函数是如何满足该需求的。相比原先的2行代码，这次稍微复杂点，变为5行。思路还是和原来一样，先格式化一个运算表达式的字符串，然后把其它工作统统丢给 eval 搞定即可。

```py
def Foo(sOperator, lstValues) :
    sExpr = "";
    for n in lstValues[1:] :  # 略过第一个元素
        sExpr += (sOperator + str(n));
    return eval(str(lstValues[0]) + sExpr);  # 补上第一个元素并求值
```

调用的时候，只需写如下这行，即可打印出 14。

```py
print Foo("+", [2,3,4,5]);

```

## 示例２

在示例２中，咱们继续把需求复杂化。

假设要实现一个类似计算器的玩意儿，让用户在【运行时】输入一个四则运算表达式并计算结果。要求支持常见的四则运算符，要求支持运算符之间的优先级（也就是小括号）。这时候，假如你企图用静态语言自己来实现该功能（不依靠第三方的库），那你得费老大老大的劲了。而用 Python，代码反而比示例１还简单（一个 eval 语句搞定）。

## 示例３

看到这里，肯定有同学不服气了：你玩来玩去，都是在搞数值运算，有没有啥新花样啊？


eval 手法当然不仅仅限于玩数字运算啦！下面就来说说 eval 如何运用于新的场合。

为了通俗易懂，俺就以邮件客户端为例（估计 99.9% 的同学都用过 Email）。邮件客户端有一个常见的需求是：用户可以自行配置一些过滤规则，用来过滤一些垃圾邮件。

假设咱们要开发的是一个比较牛逼的客户端，其过滤规则要足够强大：可以根据邮件的不同属性进行条件判定（需求人员要求支持的属性有：标题、正文、发件人、收件人、附件数）。为了体现该软件的牛X，需求人员要求：可以让用户设定各种灵活的嵌套逻辑组合。比如用户可以配置如下这条判定规则：

> 如果（（标题包含"交友" AND （发件人来自"qq.com" OR 发件人来自"kaixin.com"）） OR 附件数大于10） 就认定为垃圾邮件

当然，俺为了叙述方便，用了上面这种伪代码来阐述。真正的用户都是比较傻瓜的，咱肯定要提供一个足够傻瓜的界面来让用户配置过滤规则。

至于界面如何设计，不是本文的重点，略过不提。目前的关键问题是，如果要支持这种复杂的嵌套逻辑表达式，后台的过滤引擎要如何处理才好？估计有些同学已经看出来了，用静态语言来处理是很棘手滴——因为规则是由用户在运行时任意配置，逻辑嵌套的层次不定，邮件的属性在将来也很可能会扩展。

这时候，eval 手法又可以大放异彩了。如果用户配置了刚才那条过滤规则，那么界面模块只需要生成如下一个 Python 函数的源代码（说白了就是一个字符串）。

```py
def Filter(sTitle, sContent, sFrom, sTo, nAttachNum) :
    if (sTitle.find("交友")!=-1 and (sFrom.find("@qq.com")!=-1 or sTo.find("@kaixin.com")!=-1)) or nAttacheNum>10 :
        return True;
    else :
        return False;
```

后台模块可以先通过 Python 内置的 exec 函数，拿上述字符串创建出一个 Filter 函数。以后，每当收到一个邮件，只需把该邮件的各个属性传递给该 Filter 函数，即可完成垃圾邮件判定。

顺便说一下：喜欢 OO 风格的同学，可以把上述代码重构一下，加入一个 Mail 的类，把 Filter 作为 Mail 的一个方法；喜欢 Pythonic 风格的同学，也可以把上述代码改为更简洁的写法。

## 总结

最后，来个总结发言。这种玩法的奥妙在于：那个传递给 eval / exec 的字符串，既可以看成是【数据】，也可以看成是可执行的【代码】。在动态语言的 eval 手法中，数据和代码得到了完美的结合。有了这种结合，你就获得了【在运行时生成代码的能力】。