

Python核心技术进阶训练篇
=====================


## 第二章

### 2.1如何在列表，字典，集合中根据条件筛选数据

#### 过滤列表[-3, 4, -9, 2, -8, 7, -7, 9, 7, 1]中的负数

```py
# Step 1)随机生成10个元素的列表，每个元素的范围在-10到10之间
from random import randint
data = [randint(-10, 10) for _ in range(10)]   # python2.x 使用xrange(10)
data
[-3, 4, -9, 2, -8, 7, -7, 9, 7, 1]

# Step 2) 过滤其中的负数
# way 1
filter(lambda x: x >= 0, data)

timeit filter(lambda x: x >= 0, data)

# way 2
[x for x in data if x >= 0]
```


#### 筛选出字典{'LiLei':79, 'Jim':88, 'Lucy':92}中值高于90的项

```py
d = {x : randint(60, 100) for x in range(1,21)}
{k : v for k, v in d.items() if v >= 90}
```

#### 筛选出集合中{77, 89, 32, 20 ...}中能被3整除的元素

```py
# 列表转集合
s = set(data)
{x for x in s if x % 3 == 0}
```


### 2.2 3 4 命名  统计  字典

#### 命名案列

```py
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s1 = Student('Jim', 8, 'male', 'jim@test.com')
s2 = Student('Lucy',7, 'female', 'lucy@test.com')
```

#### 统计序列中元素出现频度

> 某随机序列[1,2,1,3 ...]中，找到出现次数最高的3个元素，它们的出现次数是多少？
```py
from random import randint
data = [randint(0, 20) for _ in range(30)]

# way 1
c = dict.fromkeys(data, 0) # 生成以data为key的字典
for x in data:
    c[x] += 1

# way 2
from collections import Counter
c2 = Counter(data)
c2.most_common(4) # 出现次数最多的前4个
```

> 对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，它们的出现次数是多少？
```py
import re
txt = open('china.txt').read()
word_list = re.split('\W', txt) # 使用正则表达式进行分割
c3 = Counter(word_list)
c3.most_common(10)
```

#### 字典排序

> 如何根据字典中值的大小，对字典中的项排序

```py
from randint import randint
d = {x: randint(60, 100) for x in 'abcdefg'}

# way 1
zip(d.v alues(), d.keys())
sorted(zip(d.values(), d.keys()))

# way 2
sorted(d.items(), key=lambda x: x[1])
```

### 2.5 公共键

> 如何快速找到多个字典中的公共键

```py
from random import randint, sample
# 产生随机球员，假设有a,b,c,d,e,f,g 7名球员
s1 = { x: randint(1,4) for x in sample('abcdeg',randint(3,6))}
s2 = { x: randint(1,4) for x in sample('abcdeg',randint(3,6))}
s3 = { x: randint(1,4) for x in sample('abcdeg',randint(3,6))}

s1
{'g': 2, 'c': 2, 'a': 4}
s2
{'g': 4, 'b': 3, 'd': 1}
s3
{'g': 1, 'a': 3, 'c': 3, 'b': 1, 'd': 4, 'e': 1}

# 一般解决方案

result = []
for k in s1:
    if k in s2 and k in s3:
        result.append(k)

result
['g']

# 利用集合(set)的交集操作

# step 1 使用字典的keys()方法，得到一个字典keys的集合

s1.keys() & s2.keys() & s3.keys()
{'g'}

# step 2 使用map函数，得到所有字典的keys的集合

map(dict.keys, [s1, s2, s3])

# step 3 使用reduce函数，取所有字典的keys的集合的交集

from functools import reduce
reduce(lambda a, b : a & b, map(dict.keys, [s1, s2, s3]))
{'g'}
```

### 2.6 如何让字典保持有序

使用OrderedDict可以保证字典按先后进入的顺序保存

```py
from collections import OrderedDict
d = OrderedDict()

d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)

for k in d: print(k)
Jim
Leo
Bob
```


### 2.7 历史记录

> 使用容量为n的队列存储历史记录

使用标准库collections中的deque， 它是一个双端循环队列

```py
from collections import deque
q = deque([], 5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q
deque([2, 3, 4, 5, 6])
```

程序退出前，可以用pickle将队列对象保存到文件，再次运行时将其导入

```py
import pickle
pickle.dump(str(q), open('history','wb'))
q2 = pickle.load(open('history','rb'))
q2
'deque([2, 3, 4, 5, 6], maxlen=5)' # type(q2) = 'str'
```


## 第三章

### 3.1 2 迭代器

> 如何实现可迭代对象和迭代器对象

某软件要求，从网络抓取各城市气温信息，并以此显示：

北京：15～20

添加：17～22

长春：12～18

如果一次抓取所有城市天气信息再显示，显示第一个城市气温时，有很高的延时，并浪费存储空间。我们期望以“用时访问”的策略，并且能把所有城市气温封装到一个对象里，可用for语句进行迭代

#### 解决方案

 - Step 1：实现一个迭代器对象WeatherIterator，next方法每次返回一个城市气温信息

 - Step 2：实现一个可迭代对象WeatherIterable， \_\_iter\_\_方法返回一个迭代器对象


```py
from collections import Iterable, Iterator
import requests

def getWeather(city):
    r = requests.get(d)
    data = r.json()['data']['forecast'][0]
    return '%s: %s , %s' %(city, data['low'], data['high'])

print(getWether('南京'))
南京: 低温 18℃ , 高温 28℃

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(d)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s' %(city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


# test
for x in WeatherIterable(['南京','北京','上海','海南','哈尔滨']):
    print(x)
```


