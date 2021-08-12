

> elasticsearch是面向文档的，关系数据库和elasticsearch客观的对比

| Relational Database | Elasticsearch |
| ------------------- | ------------- |
| 数据库(database)    | 索引(indices) |
| 表(tables)          | types         |
| 行(rows)            | documents     |
| 字段(columns)       | fields        |

elasticsearch(集群)中可以包含多个索引(数据库)，每个索引中可以包含多个类型(表)，每个类型下又包含多个文档(行)，每个文档中又包含多个字段(列)。

### 物理设计：

elasticsearch在后台把每个索引分成多个分片，每个分片可以在集群中的不通服务器迁移

###  逻辑设计：

一个索引类型中，包含多个文档，比如说文档1，文档2。当我们索引一篇文档时，可以通过这样的顺序找到它：索引》类型》文档ID，通过这个组合我们就能索引到某个具体的文档。注意ID不必是整数，实际上它是个字符串

#### 文档

elasticsearch是面向文档的，意味着索引和搜索数据的最小单位是文档， 文档有几个重要属性：

* 自我包含，一篇文档同时包含字段和对应的值，也就是同时包含key:value
* 可以是层次型的，一个文档中包含自文档，复杂逻辑实体就是这么来的；
* 灵活的结构，文档不依赖预先定义的模式，在关系数据库中，要提前定义字段表结构，在es中，对于字段是非常灵活的；

尽管我们可以随意新增或忽略某个字段，但是字段的类型却非常重要，比如一个年龄字段类型，可以是字符串也可以是整数。因为es会保存字段和类型之间的映射及其他的设置。这种映射具体到每个映射的每种类型，这也是为什么在es中，类型有时候也称为映射类型。

#### 类型

就是每个fields的数据类型，类型是文档的逻辑容器，就像关系数据库一样，表格是行的容器。类型中对于字段的定义成为映射，比如name映射为字符串。

#### 索引

就是数据库！索引是映射类型的容器，elasticsearch中的索引是一个非常大的文档集合。索引存储了映射类型的字段和其他设置。然后他们被存储到了各个分片上

#### 倒排索引

elasticsearch使用了一种称为倒排索引的结构，采用Lucene倒排索引作为底层。这种结构适用于快速的全文搜索，一个索引由文档中所有不重复的列表构成，对于每一个词，都有一个包含它的文档列表。



## ES和Solr的区别



## ElasticSearch安装

官网 https://www.elastic.com， 需要安装JDK1.8

安装好后访问 http://localhost:9200

```sh
 {
  "name" : "fc04cf0e71ec",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "Wh0OVPxjRyOsxz9Cf-DyWg",
  "version" : {
    "number" : "7.12.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "3186837139b9c6b6d23c3200870651f10d3343b7",
    "build_date" : "2021-04-20T20:56:39.040728659Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

> 安装可视化界面ES head的插件

下载地址：[mobz/elasticsearch-head: A web front end for an elastic search cluster (github.com)](https://github.com/mobz/elasticsearch-head)



## 安装ELK

语言设置设置

```sh
[root@wistreeweb docker-elk]# docker exec -it docker-elk_kibana_1 bash
bash-4.4$ cd /usr/share/kibana/x-pack/plugins/translations/translations
bash-4.4$ ls
ja-JP.json  zh-CN.json
vi /usr/share/kibana/config/kibana.yml
i18n.locale : "zh-CN"
```



### IK分词器

Download from https://github.com/medcl/elasticsearch-analysis-ik

```sh
elasticsearch-plugin list # list all installed plugins
```

unpack the download package and put it into folder elasticsearch-xxx/plugins/ik of elasticsearch, restart elasticsearch

#### 在Kibana里测试

进入到Dev Tools

```sh
GET _analyze
{
  "analyzer": "ik_smart",
  "text": "中国共产党"
}

GET _analyze
{
  "analyzer": "ik_max_word",
  "text": "中国共产党"
}
```

* ik_smart : 最少划分
* ik_max_word : 细粒度分词

> 如果输入“超级喜欢狂神说Java”，狂神说被拆开了

这种自定义关键字的情况下，需要添加自定义的字典

```sh
vi /usr/share/elasticsearch/plugins/elasticsearch-analysis-ik-7.12.1/config/IKAnalyzer.cfg.xml


```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
        <comment>IK Analyzer 扩展配置</comment>
        <!--用户可以在这里配置自己的扩展字典 -->
        <entry key="ext_dict">custom.dic</entry>
         <!--用户可以在这里配置自己的扩展停止词字典-->
        <entry key="ext_stopwords"></entry>
        <!--用户可以在这里配置远程扩展字典 -->
        <!-- <entry key="remote_ext_dict">words_location</entry> -->
        <!--用户可以在这里配置远程扩展停止词字典-->
        <!-- <entry key="remote_ext_stopwords">words_location</entry> -->
</properties>
```

add custom.dic

```sh
亲近母语
徐冬梅
狂神说
日有所诵
小步读书
```

部署custom.dic前测试 "江苏省南京市有一家文化教育公司，它的名字叫亲近母语，创始人是徐冬梅。"，返回结果为：

```json
{
  "tokens" : [
    {
      "token" : "江苏省",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "CN_WORD",
      "position" : 0
    },
    {
      "token" : "南京市",
      "start_offset" : 3,
      "end_offset" : 6,
      "type" : "CN_WORD",
      "position" : 1
    },
    {
      "token" : "有",
      "start_offset" : 6,
      "end_offset" : 7,
      "type" : "CN_CHAR",
      "position" : 2
    },
    {
      "token" : "一家",
      "start_offset" : 7,
      "end_offset" : 9,
      "type" : "CN_WORD",
      "position" : 3
    },
    {
      "token" : "文化教育",
      "start_offset" : 9,
      "end_offset" : 13,
      "type" : "CN_WORD",
      "position" : 4
    },
    {
      "token" : "公司",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "CN_WORD",
      "position" : 5
    },
    {
      "token" : "它",
      "start_offset" : 16,
      "end_offset" : 17,
      "type" : "CN_CHAR",
      "position" : 6
    },
    {
      "token" : "的",
      "start_offset" : 17,
      "end_offset" : 18,
      "type" : "CN_CHAR",
      "position" : 7
    },
    {
      "token" : "名字叫",
      "start_offset" : 18,
      "end_offset" : 21,
      "type" : "CN_WORD",
      "position" : 8
    },
    {
      "token" : "亲近",
      "start_offset" : 21,
      "end_offset" : 23,
      "type" : "CN_WORD",
      "position" : 9
    },
    {
      "token" : "母语",
      "start_offset" : 23,
      "end_offset" : 25,
      "type" : "CN_WORD",
      "position" : 10
    },
    {
      "token" : "创始人",
      "start_offset" : 26,
      "end_offset" : 29,
      "type" : "CN_WORD",
      "position" : 11
    },
    {
      "token" : "是",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "CN_CHAR",
      "position" : 12
    },
    {
      "token" : "徐",
      "start_offset" : 30,
      "end_offset" : 31,
      "type" : "CN_CHAR",
      "position" : 13
    },
    {
      "token" : "冬梅",
      "start_offset" : 31,
      "end_offset" : 33,
      "type" : "CN_WORD",
      "position" : 14
    }
  ]
}
```

部署custom.dic后并重新启动elasticsearch，测试 "江苏省南京市有一家文化教育公司，它的名字叫亲近母语，创始人是徐冬梅。"，返回结果为：

```json
{
  "tokens" : [
    {
      "token" : "江苏省",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "CN_WORD",
      "position" : 0
    },
    {
      "token" : "南京市",
      "start_offset" : 3,
      "end_offset" : 6,
      "type" : "CN_WORD",
      "position" : 1
    },
    {
      "token" : "有",
      "start_offset" : 6,
      "end_offset" : 7,
      "type" : "CN_CHAR",
      "position" : 2
    },
    {
      "token" : "一家",
      "start_offset" : 7,
      "end_offset" : 9,
      "type" : "CN_WORD",
      "position" : 3
    },
    {
      "token" : "文化教育",
      "start_offset" : 9,
      "end_offset" : 13,
      "type" : "CN_WORD",
      "position" : 4
    },
    {
      "token" : "公司",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "CN_WORD",
      "position" : 5
    },
    {
      "token" : "它",
      "start_offset" : 16,
      "end_offset" : 17,
      "type" : "CN_CHAR",
      "position" : 6
    },
    {
      "token" : "的",
      "start_offset" : 17,
      "end_offset" : 18,
      "type" : "CN_CHAR",
      "position" : 7
    },
    {
      "token" : "名字叫",
      "start_offset" : 18,
      "end_offset" : 21,
      "type" : "CN_WORD",
      "position" : 8
    },
    {
      "token" : "亲近母语",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "CN_WORD",
      "position" : 9
    },
    {
      "token" : "创始人",
      "start_offset" : 26,
      "end_offset" : 29,
      "type" : "CN_WORD",
      "position" : 10
    },
    {
      "token" : "是",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "CN_CHAR",
      "position" : 11
    },
    {
      "token" : "徐冬梅",
      "start_offset" : 30,
      "end_offset" : 33,
      "type" : "CN_WORD",
      "position" : 12
    }
  ]
}

```



## Rest风格操作

一种API架构风格，而不是标准，只是提供了一组设计原则和约束条件。主要用于客户端和服务器交互类的软件。基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制。

基本Rest命令说明：

| Method | URL 地址                                        | 描述                   |
| ------ | ----------------------------------------------- | ---------------------- |
| PUT    | localhost:9200/索引名称/类型名称/文档ID         | 创建文档（指定文档ID） |
| POST   | localhost:9200/索引名称/类型名称                | 创建文档（随机文档ID） |
| POST   | localhost:9200/索引名称/类型名称/文档ID/_update | 修改文档               |
| DELETE | localhost:9200/索引名称/类型名称/文档ID         | 删除文档               |
| GET    | localhost:9200/索引名称/类型名称/文档ID         | 通过文档ID查询文档     |
| POST   | localhost:9200/索引名称/类型名称/_search        | 查询所有数据           |

### 关于索引的基本操作

#### 创建索引

```sh
PUT /test1/type1/doc1 
{
  "name":"jezhang",
  "age":36
}
```

```json
#! [types removal] Specifying types in document index requests is deprecated, use the typeless endpoints instead (/{index}/_doc/{id}, /{index}/_doc, or /{index}/_create/{id}).
{
  "_index" : "test1",
  "_type" : "type1",
  "_id" : "doc1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

> use the typeless endpoints instead (/{index}/_doc/{id}, /{index}/_doc, or /{index}/_create/{id}). 

#### 数据类型

* 字符串类型：text , keyword
* 数值类型：     long, integer, short, byte, doulbe, float, half_float, scaled_float
* 日期类型：     date
* 布尔值类型： boolean
* 二进制类型： binary

#### 指定数据类型创建索引

```sh
PUT /test2
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "age": {
        "type": "integer"
      },
      "birthdate": {
        "type": "date"
      }
    }
  }
}
```

```json
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test2"
}
```

获得索引信息

```sh
GET test2
```

```json
{
  "test2" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "age" : {
          "type" : "integer"
        },
        "birthdate" : {
          "type" : "date"
        },
        "name" : {
          "type" : "text"
        }
      }
    },
    "settings" : {
      "index" : {
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "number_of_shards" : "1",
        "provided_name" : "test2",
        "creation_date" : "1622112962352",
        "number_of_replicas" : "1",
        "uuid" : "heuH_JuqSpC32TsmeKlsoA",
        "version" : {
          "created" : "7120199"
        }
      }
    }
  }
}
```

默认创建文档_doc

```sh
PUT /test3/_doc/1
{
  "name":"环紫金山",
  "age": 35,
  "birthdate":"1997-01-05"
}
```

```json
{
  "_index" : "test3",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}

```

自定义过滤器，过滤html标签

```sh
PUT index_with_filter
{
  "settings": {
    "analysis": {
      "analyzer": {
        "html_text_analyzer": {
          "tokenizer": "standard",
          "char_filter": [
            "html_char_filter"
          ]
        },
        "html_keyword_analyzer": {
          "tokenizer": "keyword",
          "filter": [
            "trim"
          ],
          "char_filter": [
            "html_char_filter"
          ]
        }
      },
      "char_filter": {
        "html_char_filter": {
          "type": "html_strip"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "fields": {
          "html_text": {
            "search_analyzer": "simple",
            "analyzer": "html_text_analyzer",
            "type": "text"
          },
          "html_keyword": {
            "analyzer": "html_keyword_analyzer",
            "type": "text"
          }
        }
      }
    }
  }
}
```



#### Elasticsearch扩展命令

```sh
GET _cat/health  # 获取数据库健康值
GET _cat/indices
```

#### PUT修改索引值(过时的方法)

```sh
PUT /test3/_doc/1
{
  "name":"环紫金山123",
  "age": 35,
  "birthdate":"1997-01-05"
}
```

```json
{
  "_index" : "test3",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

POST修改索引

```sh
POST /test3/_doc/1/_update
{
  "name":"环紫金山234",
  "age": 35,
  "birthdate":"1997-01-05"
}
```

```json
#! [types removal] Specifying types in document update requests is deprecated, use the endpoint /{index}/_update/{id} instead.
{
  "_index" : "test3",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 3,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 2,
  "_primary_term" : 1
}
```

#### 删除索引

```sh
delete test1
```

```json
{
  "acknowledged" : true
}
```



### 关于文档的基本操作

> 基本操作

1、添加数据

```sh
PUT kuangshen/user/1
{
  "name":"狂神说",
  "age":23,
  "desc": "一顿操作猛如虎，一看工资2500",
  "tags": ["技术宅", "温暖", "直男"]
}

PUT kuangshen/user/2
{
  "name":"张三",
  "age":25,
  "desc": "法外狂徒",
  "tags": ["交友", "旅游", "渣男"]
}

PUT kuangshen/user/3
{
  "name":"李四",
  "age":30,
  "desc": "不知道如何形容",
  "tags": ["靓女", "旅游", "唱歌"]
}

# 更新数据
POST kuangshen/user/1/_update
{
  "doc": {
    "name": "狂神说Java"
  }
}

# 查询
GET kuangshen/user/_search?q=name:狂神说
GET kuangshen/user/_search?q=name:狂神说Java
```



> 高级操作

排序，分页，高亮，模糊查询，精准查询

```sh
GET kuangshen/user/_search
{
  "query": {
    "match": {
      "name": "狂神"
    }
  },
  "sort": [
    {
      "age": {
        "order": "desc"
      }
    }
  ],
  "from": 0,
  "size":1,
  "_source": ["name", "age", "asc"]
}



# 布尔值查询

GET kuangshen/user/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "name": "狂神说"
          }
        },
        {
          "match": {
            "age": 23
          }
        }
      ]
    }
  }
}


```



#### 集成SpringBoot



### 实战

#### 爬虫

#### 前后端分离

#### 搜索高亮



