

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

### 2.5

### 2.6

### 2.7