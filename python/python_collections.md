collections
===========

collections是Python标准库的一部分，可以通过：

```python
import collections 
```

来使用这个标准库，这个库定义了几个方便的数据结构，可以极大地提高处理数据时的效率。

### namedtuple

nameedtuple有一个中文名字，叫作“具名元祖”，代表这是一个每个值都有名字的元组，比如有如下这样一个元组：

```python
t = ('jilu', '27', 'Beijing')
```

只用这个元组时，我们不得不使用下标来取值，比如取我的名字时可以使用t[0]，这样不仅麻烦，而且还增加了记忆负担。那么给每个值都起一个名字，取值的时候不就方便了么？因此，也就有了字典这个数据结构，就像下面这样：

```python
>>> kt = ('name', 'age', 'loc')
>>> d4 = dict(zip(kt, t))
>>> d4
{'loc': 'Beijing', 'age': '27', 'name': 'jilu'}
```

这里用的是另外一种定义字典的方式，该方法结合使用了zip()和dict()这两个方法，即将一个keys的元组与一个values的元组结合成一个字典。现在取我的名字时就可以通过d4['name']或d4('name')来取得了。不过这样很麻烦，因为要打一对括号和引号，而且实际上Python字典存储数据的空间利用率只有一半，那么有没有更好的方法呢？有，那就是具名元组，可以通过定义一个具名元组来实现，示例如下：

```python
>>> from collections import namedtuple
>>> nt = namedtuple('nt', 'name age loc')
>>> nt1 = nt('jilu', '27', 'Beijing')
>>> nt1
nt(name='jilu', age='27', loc='Beijing')
>>> nt1.name
'jilu'
```


### Counter

Counter是一个累加器，可以用来做经典的word count，比如：

```python
>>> doc = """Just when you thought it was safe to got the deepest part of the ocean...it isn't. It's really hard, don't go there. But if you did get to Challenger Deep in the Mariana Trench, thought to be one of the deepest parts of the ocean, what you heard might scare your waterproof socks off."""
>>> 
>>> word_list = doc.split()
>>> from collections import Counter
>>> cc = Counter(word_list)
>>> cc
Counter({'the': 5, 'to': 4,'you': 3, 'of': 3, 'go': 2, 'deepest': 2, 'thought': 2, 'it': 1, 'socks': 1})
>>> for k,v in cc.most_common():
...     print(k, v)
...
('the', 5)
('to', 4)
('you', 3)
('of', 3)
('go', 2)
...
>>>     
```

可以看到，一个Counter对象和字典颇为相似，实际上Counter就是字典类型的一个子类。我们先用split()方法将原始的英文文本进行分词，然后将包含全部单词的列表作为Counter的参数，最终通过for循环打印Counter对象most_common()方法的返回值，这个方法类似于字典的items方法，只不过它会按照每个单词出现次数的多少进行排序，之后再将结果进行输出。

### defautdict

在difaultdict中，可以为一个字典的值设定一个默认值，比如当默认值为空列表时：
```python
>>> from collections import defaultdict
>>> cl = defaultdict(list)
>>> cl['key']
[]
>>> cl['key'].append(1)
>>> cl['key'].append(2)
>>> cl['key'].append(3)
>>> cl['key1'].append(4)
>>> cl
defaultdict(<type 'list'>, {'key1':[4], 'key':[1, 2, 3]})
```

其实与其等效的Python代码也并不算太复杂，与上一个例子Counter的代码类似，只要判断某个键值是否存在，如果不存在则赋值一个默认值，这样也可以实现相应的功能。

### OrderedDict

通常情况下，Python的字典是无序的散列表，不过有些时候我们希望保留数据被添加字典的顺序，这样就可以让我们在之后迭代的时候还原原来的顺序，这个时候就需要OrderedDict这个数据结构了，现在，使用这个数据结构的方式共有两种，第一种是按顺序添加：

```python
d = {}
cc = OrderedDict()
for x in ["b", "a", "h", "d"]:
    cc[x] = 1
    d[x] = 1

for x in range(len(d)):
    print(d.keys()[x], cc.keys()[x])

# 运行结果如下：
a b
h a
b h
d d
```

上面的结果中第一列是普通的字典，第二列是有序字典，可以看到第二列的顺序没有改变。除了这种方式之外，与dict()函数一样，OrderedDict也接受一个元组组成的序列作为参数，并且保持元组的顺序，示例如下：

```python
tuple_list = zip(["b", "a", "h", "d"], [1]*4)
print(tuple_list)
for k,v in OrderedDict(tuple_list).items():
# 运行结果如下：
b 1
a 1
h 1
d 1
```

可以看到这里的结果顺序与创建字典时的顺序一致，这就是使用OrderedDict带来的额外好处。





