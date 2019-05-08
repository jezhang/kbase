Redis入门指南
============

## 1 准备

### 1.1 安装

#### 在POSIX系统中安装

```sh
wget http://download.redis.io/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable
make
```

#### 在OS X系统中安装

```sh
brew install redis
```

### 第二章 Redis API的使用和理解

#### 通用命令

##### 通用命令

```sh
keys
# 编列所有key，使用通配符[*,?]
# keys 命令一般不要在生产环境使用，时间复杂度为O(n)，因为是单线程，会阻塞其它的命令

dbsize
# 计算key的总数，时间复杂度为O(1)，可在生产环境随便使用

exists key
# 检查key是否存在，存在返回(integer)1，否则返回(integer)0
# 时间复杂度O(1)

del key [key ...]
# 删除指定key-value，可以删除多个
# 时间复杂度O(1)

expire key seconds
# 设置key在seconds秒后过期
# 时间复杂度O(1)
ttl key
# 查看key剩余的过期时间
(integer)-2
# -2 代表key已经不存在了
persist key
# 去掉key的过期时间
# 执行ttl key 返回(integer) -1
# -1 代表key存在，并且没有过期时间

type key
# 查看数据类型
# 时间复杂度O(1)
set a b
type a
string

sadd myset 1 2 3
type myset
set
```

##### 数据结构和编码

```sh
string(raw, int, embstr)
hash(hashtable, ziplist)
list(linkedlist, ziplist)
set(hashtable, intset)
zset(skiplist, ziplist)
```

##### 单线程

redis在任何一个瞬间只会执行1个命令

#### 字符串类型

```sh
incr key
# key自增1，如果key不存在，自增后get(key)=1
decr key
# key自剪1，如果key不存在，自减后get(key)=-1
incrby key k
# key自增k，如果key不存在，自增后get(key)=k
decr key k
# key自剪k，如果key不存在，自减后get(key)=-k
```

##### 实战：缓存视频的基本信息（数据源在MySQL中）伪代码

```java
public VideoInfo get(int id) {
    String redisKey = redisPrefix + id;
    VideoInfo videoInfo =  redis.get(redisKey);
    if(videoInfo == null) {
        videoInfo = mysql.get(id);
        if(null != videoInfo) {
            // serializer
            redis.set(redisKey, serializer(videoInfo))
        }
    } else {
        return deserializer(videoInfo)
    }
}
```

```sh
set key value
# 不管key是否存在，都设置，时间复杂度O(1)
setnx key value
# key不存在，才设置，时间复杂度O(1)
set key value xx
# key存在，才设置，时间复杂度O(1)

mget key1 key2 key3
# 批量获取key，原子操作，时间复杂度O(n)

mset key1 value1 key2 value2 key3 value3
# 批量设置key value，原子操作，时间复杂度O(n)

getset key newvalue
# set key newvalue并返回旧的value，原子操作， 时间复杂度O(1)

append
# 将value追加到旧的value，返回长度，时间复杂度O(1)

strlen
# 返回字符串的长度（注意中文占用2个字节），时间复杂度O(1)
set football "足球"
strlen football
(integer) 4

incrbyfloat key 3.5
# 增加key对应的值3.5，时间复杂度O(1)

getrange key start end
# 获取字符串指定下标所有的值，时间复杂度O(1)

setrange
# 设置指定下标所有对应的值，时间复杂度O(1)
```

#### hash

```sh
hget key field
# 获取hash key对应field的value, 时间复杂度o(1)

hset key field value
hsetnx 
# 设置hash key对应field的value, 时间复杂度o(1)

hdel key field
# 删除hash key对应field的value, 时间复杂度o(1)

hexists key field
# 判断hash key是否有field

hlen key
# 获取hash key field的数量

hmget key field1 field2 ... fieldN
# 批量获取hash key的一批field对应的值, 时间复杂度o(n)

hmset key field1 value1 field2 value2 ...
# 批量设置hash key的一批field value, 时间复杂度o(n)

hgetall
# 返回hash key对应所有的field和value, 时间复杂度o(n)，数据量大时小心使用

hvals
# 返回hash key对应所有的field的value, 时间复杂度o(n)

hkeys
# 返回hash key对应所有field, 时间复杂度o(n)

```

#### List

```sh
rpush key value1 value2 ... valueN
# 从列表右端插入值(1-N), 时间复杂度o(1~n)


lpush key value1 value2 ... valueN
# 从列表左端插入值(1-N), 时间复杂度o(1~n)

linsert key before|after value newValue
# 在list指定的值前|后插入newValue，时间复杂度o(n)

lpop key
# 从列表左侧弹出一个item，时间复杂度o(1)

rpop key
# 从列表右侧弹出一个item，时间复杂度o(1)

lrem key count value
# 根据count值，从列表中删除所有value相等的项,o(n)

ltrim key start end
# 安装索引范围修剪列表,o(n)

lrange key start end
# 获取列表指定索引范围所有item,o(n)

llen
# 获取列表长度,o(1)

lset key index newValue
# 设置列表指定索引值为newValue


```

#### set

```sh
sadd key element
# 向集合key添加element(如果element已经存在，添加失败), O(1)

srem key element
# 将集合key中的element移除掉

smembers key

```

#### zset有序集合

```sh
zadd key element
# 添加元素

zrem key element
# 删除元素o(1)
```

##### 结构和命令

##### 内部编码

##### 快速实战

##### 查缺补漏

#### 哈希类型

#### 列表类型

#### 集合类型

#### 有序集合类型
