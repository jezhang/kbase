
## 数据库重构过程

本章描述了如何在你的数据库中实现一次重构。我们通过一个例子来进行“移动列”重构，这是一种结构重构。尽管这看起来像是一种简单的重构，它也确实是这样，但是你会看到，在生产环境中安全地实现这种重构可能相当复杂。图3.1从总体上描述了我们如何将Cus-tomer.Balance列移动到Account表，这是改进数据库设计的一种直接变更。

![](https://asdfex.oss-cn-qingdao.aliyuncs.com/picgo/20230131210300.png)

### 3.1 验证数据库重构是否合适

重构是否需要进行。有以下3个问题需要考虑：

1. 这个重构有意义吗？

2. 变更真的需要现在进行吗？

3. 值得这样去做吗？

### 3.2 选择最合适的数据库重构

### 3.3 让原来的数据库 schema 过时

如果有多个应用访问你的数据库，你需要在这样一种假定下工作，即你不能在重构之后同时部署所有这些程序。你需要一个转换期，也被称为过时期，在这期间保持你打算改动的原来的schema部分。在这个转换期中，你同时支持原来的schema和新的schema，给其他应用团队留出时间来重构并部署他们的系统。这一点暗示我们需要将这一过程尽可能地自动化。

在转换期中，你需要假定两件事情：首先，某些应用会使用原来的schema，而另外一些应用会使用新的schema；

并非所有的数据库重构都需要转换期。例如，“引入列约束”和“采用标准编码”这两种数据库重构就不需要转换期，因为他们只是通过缩小列接收值的范围，对数据质量进行改进。缩小值的范围可能会破外现有的应用，这些重构要小心。