PostgresSQL SQL调优技巧
=====================

## SQL调优范式

### 开发范式一：不要轻易把字段嵌入到表达式

在salary列上有index，但是条件语句中把salary列放在了表达式当中，导致索引被压抑，因为索引里面存储的是salary的值，而不是salary加上100以后的值。
```sql
explain select * from emp where salary + 100 = 2000; 
--------------------------------------------------------------------
Gather (cost=1000.00..7796.60 rows=2294 width=36)
  Workers Planned: 2
  -> Parallel Seq Scan on emp (cost=0.00..6567.20 rows=956 width=36)
       Filter: ((salary + 100) = 2000)
(4 rows)
```
通过等式转换，把salary列从表达式中剥离出来，就会用到索引。
```sql
explain select * from emp where salary = 2000 - 100;
--------------------------------------------------------------------
Index Scan using emp_salary_index on emp (cost=0.42..8.44 rows=1 width=36)
  Index Cond: (salary = 1900)
(2 rows)
```

### 开发范式二：不要轻易把字段嵌入到函数中
在hiredate列上有index，但是条件语句中把该列放在了函数当中，导致索引被压抑，因为索引里面存储的是该列的值，而不是函数处理以后的值。
```sql
explain select * from emp where to_char(hiredate, ‘dd-mm-yyyy’)=’22-05-2022’;
--------------------------------------------------------------------
Seq Scan on emp (cost=0.00..289.32 rows=50 width=62)
  Filter: (to_char((hiredate)::timestamp with time zone, 'dd-mm-yyyy'::text) = '22-05-2022'::text)
```
改写成（通过等式转换，把列从函数中剥离出来，就会用到索引，比较成本，差别较大）
```sql
explain select * from emp where hiredate = to_date(’22-05-2022’, ‘dd-mm-yyyy’);
--------------------------------------------------------------------
Index Scan using emp_hiredate on emp (cost=0.29..8.30 rows=1 width=62)
  Index Cond: (hiredate = to_date('22-05-2022'::text, 'dd-mm-yyyy'::text))
```

### 开发范式三

如果查询中比较固定查询某些列，可以基于这几个列建符合索引，直接查询索引，避免**回表扫描**。

```sql
create index emp_empno on emp(empno, salary);
explain select empno, salary from emp where empno=7788;
--------------------------------------------------------------------
Index Only Scan using emp_empno on emp (cost=0.29..10.09 rows=2 width=8)
  Index Cond: (empno=7788)
```

## 多表查询调优技巧

## 多表查询应用案例

