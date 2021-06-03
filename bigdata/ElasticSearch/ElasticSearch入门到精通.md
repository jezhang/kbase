# 入门

## 环境准备

https://soulteary.com/2020/05/04/use-docker-to-build-elk-environment.html

## 倒排索引

> Type类型概念不复存在

## 索引操作

### 创建索引

对比关系型数据库，创建索引就等同于创建数据库

向ES服务器发送PUT请求：

```sh
PUT shopping
```

PUT 操作是幂等性的，POST操作不是幂等性的

### 查询索引

GET请求查看索引，地址不变

查看所有索引

```sh
GET _cat/indices?v
```

### 删除索引

DELETE操作用来删除索引

## 文档操作

### 创建文档

向ES服务器发送POST请求，多次发送会返回不同的_id，操作不是幂等性的

```json
POST /shopping/_doc
{
    "title":"小米手机",
    "category":"小米",
    "images":"http://www.xxx.com/yyy.jpg",
    "price": 3999.00
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "Eabs03kBRKHgPXwyb_2w",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 15
}

```

生产自定义的id, 多次执行会返回相同结果，但是_version会自动改变，这种操作是幂等性的。

```json
POST /shopping/_doc/1001
{
    "title":"小米手机",
    "category":"小米",
    "images":"http://www.xxx.com/yyy.jpg",
    "price": 3999.00
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1001",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 15
}

```

同样PUT方法也可以

```JSON
PUT /shopping/_doc/1002
{
    "title":"小米手机",
    "category":"小米",
    "images":"http://www.xxx.com/yyy.jpg",
    "price": 3999.00
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1002",
  "_version" : 3,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 7,
  "_primary_term" : 15
}
```

另外一种方式创建，把 doc 改成 create

```json
PUT /shopping/_create/1003
{
    "title":"小米手机",
    "category":"小米",
    "images":"http://www.xxx.com/yyy.jpg",
    "price": 3999.00
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1003",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 8,
  "_primary_term" : 15
}
# 第二次执行时候会报错
{
  "error" : {
    "root_cause" : [
      {
        "type" : "version_conflict_engine_exception",
        "reason" : "[1003]: version conflict, document already exists (current version [1])",
        "index_uuid" : "oTpeFBCJR7GppRJcHx0h0g",
        "shard" : "0",
        "index" : "shopping"
      }
    ],
    "type" : "version_conflict_engine_exception",
    "reason" : "[1003]: version conflict, document already exists (current version [1])",
    "index_uuid" : "oTpeFBCJR7GppRJcHx0h0g",
    "shard" : "0",
    "index" : "shopping"
  },
  "status" : 409
}
```

### 查询文档

```json
GET /shopping/_doc/1003
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1003",
  "_version" : 1,
  "_seq_no" : 8,
  "_primary_term" : 15,
  "found" : true,
  "_source" : {
    "title" : "小米手机",
    "category" : "小米",
    "images" : "http://www.xxx.com/yyy.jpg",
    "price" : 3999.0
  }
}
```

查询索引下面的所有文档

```json
GET /shopping/_search
# response
{
  "took" : 916,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "Eabs03kBRKHgPXwyb_2w",
        "_score" : 1.0,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      },
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1001",
        "_score" : 1.0,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      },
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1002",
        "_score" : 1.0,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      },
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1003",
        "_score" : 1.0,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      }
    ]
  }
}

```

### 修改文档

完全修改(操作时幂等性的，使用PUT方法)

```json
PUT /shopping/_doc/1003
{
    "title":"HUAWEI手机",
    "category":"华为",
    "images":"http://www.xxx.com/yyy.jpg",
    "price": 4999.00
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1003",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 9,
  "_primary_term" : 15
}
```



局部修改(不是幂等性的，使用POST方法)

```json
POST /shopping/_update/1002
{
    "doc" : {
      "title" : "Apple手机",
      "category": "Apple",
      "price" : 5999.00
    }
}
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1002",
  "_version" : 4,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 10,
  "_primary_term" : 15
}

```

### 删除文档

使用DELETE方法删除文档

```json
DELETE /shopping/_doc/1003
# response
{
  "_index" : "shopping",
  "_type" : "_doc",
  "_id" : "1003",
  "_version" : 3,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 15,
  "_primary_term" : 15
}
```

## 查询

### 条件查询

通过请求路径来查询

```json

GET /shopping/_search?q=category:小米
# response
{
  "took" : 14,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.2814485,
    "hits" : [
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "Eabs03kBRKHgPXwyb_2w",
        "_score" : 1.2814485,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      },
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1001",
        "_score" : 1.2814485,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      }
    ]
  }
}
```

通过请求body来查询，更推荐使用这种方式，因为路径查询受长度限制，还有中文编码问题

```json
GET /shopping/_search
{
  "query" : {
    "match" : {
      "category": "APPLE"
    }
  }
}
# response
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.2310667,
    "hits" : [
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1002",
        "_score" : 1.2310667,
        "_source" : {
          "title" : "苹果手机",
          "category" : "APPLE",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 5999.0
        }
      }
    ]
  }
}
```

全量查询

```json
GET /shopping/_search
{
  "query" : {
    "match_all" : {

    }
  }
}
# response
# 返回所有结果
```

### 分页查询

```json
GET /shopping/_search
{
  "query" : {
    "match_all" : {

    }
  },
  "from" : 0,
  "size" : 1,
}
# response
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "Eabs03kBRKHgPXwyb_2w",
        "_score" : 1.0,
        "_source" : {
          "title" : "小米手机",
          "category" : "小米",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 3999.0
        }
      }
    ]
  }
}
```

指定字段查询

```json
GET /shopping/_search
{
  "query" : {
    "match_all" : {

    }
  },
  "from" : 0,
  "size" : 1,
  "_source" : ["title", "price"]
}
```

对返回结果进行排序

```json
GET /shopping/_search
{
  "query" : {
    "match_all" : {

    }
  },
  "_source" : ["title", "price"],
  "sort" : {
    "price" : {
      "order" : "desc"
    }
  }
}
```

### 多条件查询 & 范围查询

AND操作使用must

```json
GET /shopping/_search
{
  "query" : {
    "bool" : {
      "must" : [
        {
          "match": {
            "category": "小米"
          }
        },
        {
          "match": {
            "price": 1999
          }
        }
      ]
    }
  },
  "_source" : ["title", "price"],
  "sort" : {
    "price" : {
      "order" : "desc"
    }
  }
}
```

OR操作使用should

```json
GET /shopping/_search
{
  "query" : {
    "bool" : {
      "should" : [
        {
          "match": {
            "category": "小米"
          }
        },
        {
          "match": {
            "category": "华为"
          }
        }
      ]
    }
  },
  "_source" : ["title", "price"],
  "sort" : {
    "price" : {
      "order" : "desc"
    }
  }
}
```

范围查询使用filter

```json
GET /shopping/_search
{
  "query" : {
    "bool" : {
      "should" : [
        {
          "match": {
            "category": "小米"
          }
        },
        {
          "match": {
            "category": "华为"
          }
        }
      ],
      "filter": {
        "range": {
          "price": {
            "gte": 4000,
            "lte": 6000
          }
        }
      }
    }
  },
  "_source" : ["title", "price"],
  "sort" : {
    "price" : {
      "order" : "desc"
    }
  }
}
```





### 全文检索 & 完全匹配 & 高亮查询

全文检索

```json
GET /shopping/_search
{
  "query": {
    "match": {
      "title": "手机"
    }
  }
}
# 返回所有title包含手机的记录
```

完全匹配

```json
GET /shopping/_search
{
  "query": {
    "match_phrase": {
      "category": "小华"
    }
  }
}
```

高亮查询

```json
GET /shopping/_search
{
  "query" : {
    "match" : {
      "category": "APPLE"
    }
  },
  "highlight": {
    "fields": {
      "category": {
        
      }
    }
  }
}
# response
{
  "took" : 139,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.7844853,
    "hits" : [
      {
        "_index" : "shopping",
        "_type" : "_doc",
        "_id" : "1002",
        "_score" : 1.7844853,
        "_source" : {
          "title" : "苹果手机",
          "category" : "APPLE",
          "images" : "http://www.xxx.com/yyy.jpg",
          "price" : 5999.0
        },
        "highlight" : {
          "category" : [
            "<em>APPLE</em>"
          ]
        }
      }
    ]
  }
}

```



### 聚合查询



### 映射关系









