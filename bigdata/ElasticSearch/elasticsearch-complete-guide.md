
## Section 3: Managing Documents

### Creating & deleting indices



```json
# Delete an index
DELETE /pages

# Create index with specify index settings
PUT /products
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}
```



###  Indexing documents

```json
POST /products/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10
}

# create document with id 100
POST /products/_doc/100
{
  "name": "Toaster",
  "price": 49,
  "in_stock": 5
}
```

### Retrieve documents by ID

```sh
curl -XGET "http://elasticsearch:9200/products/_doc/100"
```

### Updating documents

decrease the in_stock value to 3 for ID 100

```sh
POST /products/_update/100
{
  "doc": {
    "in_stock": 3
  }
}
```

define new field for ID 100

```sh
POST /products/_update/100
{
  "doc": {
    "tags": ["electronics"]
  }
}
```

### Scripted updates

```sh
POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock--"
  }
}

POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock = 10"
  }
}
```

use parameter

```sh
POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock -= params.qty",
    "params": {
      "qty": 4
    }
  }
}
```

multiple lines scripts

```sh
POST /products/_update/100
{
  "script": {
    "source": """
      if (ctx._source.in_stock == 0) {
        ctx.op = 'noop';
      }
      ctx._source.in_stock--;
    """
  }
}

POST /products/_update/100
{
  "script": {
    "source": """
      if (ctx._source.in_stock > 0) {
        ctx._source.in_stock--;
      }
    """
  }
}

# delete the document when in_stock <= 1
POST /products/_update/100
{
  "script": {
    "source": """
      if (ctx._source.in_stock <= 1) {
        ctx.op = 'delete';
      }
      ctx._source.in_stock--;
    """
  }
}
```



### Upserts

upserting means to conditionally update or insert a document based on whether or not

```sh
POST /products/_update/101
{
  "script": {
    "source": "ctx._source.in_stock++"
  },
  "upsert": {
    "name": "Blender",
    "price": 399,
    "in_stock": 5
  }
}
```

When run the script above, the first time will create a document due to 101 not existed, the second time will execute update.

### Replacing documents

```sh
PUT /products/_doc/100
{
  "name": "Toaster",
  "price": 79,
  "in_stock": 4
}
```

### Deleting documents

```sh
DELETE /products/_update/101
```

### Understanding routing



### How Elasticsearch reads data



### How Elasticsearch writes data



### Understanding document versioning



### Optimistic concurrency control



### Update by query



