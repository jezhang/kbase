# Linux Shell Scripting Cookbook

## 第1章 小试牛刀

### 1.1 简介
shell脚本通常是以一个以#!起始的文本文件，如下所示
```sh
#!/bin/bash
```

### 1.2 终端打印
echo是用于终端打印的基本命令
```sh
$ echo "Welcome to Bash"
$ echo Welcome to Bash
$ echo 'text in quote'
```

如果你希望打印!，不要将其放入双引号中，或者可以在其之前加入一个特殊的转义字符(\)将!转义

```sh
$ echo Hello world !
$ echo 'Hello world !'
$ echo "Hello world \!" #Escape character \ prefixed.

#另一个可用于终端打印的命令是printf。它使用的参数和C语言中的printf的函数一样
$ printf "Hello world"
$ printf "%-5s %-10s %-4s\n" No Name Mark
```

### 1.3 变量和环境变量

对于每个进程，在其运行时的环境变量可以使用下面的命令来查看
```sh
$ cat /proc/$PID/environ
# 可以使用pgrep命令获得程序的进程ID
$ pgrep java
4045
$ cat /proc/4045/environ
LESSKEY=/etc/lesskey.binNNTPSERVER=newsINFODIR=/usr/local/info:/usr/share/info:/usr/infoMANPATH=/usr/share/man:/usr/local/manHOSTNAME=SSCSUSE-Jean

$ cat /proc/4045/environ  | tr '\0' '\n'
LESSKEY=/etc/lesskey.bin
NNTPSERVER=news
INFODIR=/usr/local/info:/usr/share/info:/usr/info
MANPATH=/usr/share/man:/usr/local/man
HOSTNAME=SSCSUSE-Jean
```

一个变量可以通过以下方式进行赋值：
```sh
$ var=value           # right
$ var=hello world     # wrong
$ var="Hell world"    # right
# 输出
$ echo $var
$ echo ${var}

# 设置环境变量
HTTP_PROXY=http://192.168.0.2:3128
$ export HTTP_PROXY
$ echo $PATH
/sbin:/usr/sbin:/usr/local/sbin:/root/bin:/usr/local/bin

# 获取字符串长度
$ length=${#var}

# 获取当前shell版本
$ echo $SHELL
$ echo $0

# 检查是否为超级用户root，UID是一个重要的环境变量，可以用于检查当前脚本的执行者是否以超级管理员的身份来运行的
# root用户的UID为0
$ if [$UID -ne 0]; then
$     echo Non root user. please run as root
$ else
    echo "Root User"
fi

```

### 1.4 通过shell进行数学运算

```sh
#!/bin/bash
$ no1=4
$ no2=5
$ let result=no1+no2
$ echo $result

$ let no1++
$ let no1--

$ let no1+=6 # equals let no=no+6
$ let no1-=6 # equals let no=no-6

$ result=$[no1 + no2]
$ result=$[$no1 + 5]
$ result=$((no1 + 50))

$ result='expr 3 + 4'
$ result=$(expr $no1 + 5)

#执行浮点数计算
$ echo "4 * 0.56" | bc

no=54;
result='echo "$no * 1.5" | bc'

echo "scale=2;3/8" | bc
```

### 1.5 文件描述符和重定向

* 0 : stdin     (标准输入)
* 1 : stdout    (标准输出)
* 2 : stderr    (标准错误)

```sh
$ echo "This is a sample text 1" > temp.txt   # 第二次执行会清空第一次的内容
$ echo "This is a sample text 2" >> temp.txt  # 文本会追加到目标文件中

$ ls +
ls: cannot access +: No such file or directory
# 这里 +是一个非法参数，因此将返回错误信息

$ ls + > out.txt
ls: cannot access +: No such file or directory #将stderr文本打印到屏幕上，而不是文件中
$ ls + 2> out.txt #将错误重定向到out.txt中
$ cmd 2>stderr.txt 1>stdout.txt 

# 将stderr转换成stdout，stderr和stdout都被重定向到同一个文件中
$ cmd >output.txt 2>&1
# 或者
$ cmd &> output.txt 

$ cmd 2> /dev/null
# 来自stderr的输出被丢到文件/dev/null中。/dev/null是一个特殊的设备文件，这个文件接收到的任何数据都会被丢弃
```

从stdin读取输入的命令有多种方式接收数据

```sh
# 利用cat和管道来定制我们自己的文件描述符
$ cat file | cmd
$ cmd1 | cmd2

# 将文件重定向到命令
$ cmd < file

# 重定向脚本内部的文本块
$ cat <<EOF>log.txt
hello
world
EOF

$ cat log.txt
hello
world
```

### 1.6 数组和关联数组

```sh
$ array_var=(1 2 3 4 5) # 以0为起始索引

# 将数组定义成一组索引-值(key value pair)
$ array_var[0]="test1"
$ array_var[1]="test2"
$ array_var[2]="test3"
$ array_var[3]="test4"
$ array_var[4]="test5"
$ array_var[5]="test6"

$ echo ${array_var[0]}
test1

index=5
$ echo ${array_var[$index]}
test6

# 以清单形式打印出数组中的所有值
$ echo ${array_var[*]}
test1 test2 test3 test4 test5 test6
# 或者
$ echo ${array_var[@]}
test1 test2 test3 test4 test5 test6
# 打印数组长度
$ echo ${#array_var[*]}
6
```

定义关联数组

```sh
declare -A ass_array

#1)利用内嵌索引-值列表法，提供一个索引-值列表:
$ ass_array([index1]=val1 [index2]=val2)

#2)使用独立的索引-值进行赋值:
ass_array[index1]=val1
ass_array[index2]=val2

#列出数组索引
$ echo ${!array_var[*]}
$ echo ${!array_var[@]}
```

### 1.7 使用别名

别名有多种实现方式，可以使用函数，也可以使用alias命令

```sh
$ alias new_command='command sequence'
$ alias install='sudo apt-get install'
# so, 我们可以使用 install pidgin代替sudo apt-get install pidgin了

# alias命令的作用是暂时的。一旦关闭终端，所有设置过的别名就失效了。
# 为了使别名设置一直保持作用，可以将它放入~/.bashrc文件中
$ echo 'alias cmd="command seq"' >> ~/.bashrc

# 例：创建一个rm，它能够删除原始文件，同时在backup目录中保留副本
alias rm='cp $@ ~/backup; rm $@'
```

### 1.8 获取终端信息

获取终端的行数和列数：
tput cols
tput lines
打印出当前终端名：
tput longname
将光标移动到方位(100,100)处：
tput cup 100 100
设置终端背景色：(no可以在0到7之间)
tput setb no
设置终端前景色：(no可以在0到7之间)
tput setf no
设置文本样式为粗体：
tput bold
设置下划线的开闭：
tput smu1
tput rmu1
删除当前光标位置到行尾的所有内容：
tput ed
在输入密码时，不能让输入的内容显示出来，下面的例子中，使用stty来实现这一要求
```sh
#!/bin/sh
#Filename: password.sh
echo -e "Enter password: "
stty -echo
read password
stty echo
echo
echo Password read.
echo $password
```

### 1.9 获取、设置日期和延时

```sh
# 读取日期
$ date
Fri, Oct 16, 2015  3:12:27 PM

# 打印纪元时(从世界标准时间1970年1月1日0时0分0秒起至当前时刻的总秒数)
$ date +%s
1444979591

# 将日期转换成纪元时：
$ date --date "Fri, Oct 16, 2015  3:12:27 PM" +%s
1444979547

# 将日期串作为输入获取给定日期是星期几
date --date "Fri, Oct 16, 2015  3:12:27 PM" +%A
```

#### 日期格式字符串列表
<pre>
%a(Sat)星期
%A(Saturday)星期
%b(Nov)月
%B(November)月
%d(31)日
%d(10/18/10)固定格式日期(mm/dd/yy)
%y(10)年
%Y(2010)年
%I或%H(08)小时
%M(33)分钟
%S(10)秒
%N(695208515)纳秒
%s(1290049486)UNIX纪元时间(以秒为单位)
</pre>

```sh
$ date "+%d %B %Y"
16 October 2015

# 设置日期和时间
# date -s "21 June 2009 11:01:22"
```

### 1.10 调试脚本
```sh
$ bash -x script.sh
```

-x 标识将脚本中执行过的每一行都输出到stdout

* set -x:在执行时显示参数和命令
* set +x:禁止调试
* set -v:当命令进行读取时显示输入
* set +v:禁止打印输入

```sh
#!/bin/bash
#filename:debug.sh
for in in {1..6}
do
    set -x
    echo $i
    set +x
done
echo "Script excuted"
```

### 1.11 函数和参数
```sh
fname() 
{
    echo $1, $2;    # 访问参数1和参数2
    echo "$@";      # 以列表方式一次性打印所有参数
    echo "$*";      # 类似于$@，但参数被作为单个实体
    return 0;       # 返回值
}
```

读取命令返回值（状态）
```sh
cmd;
echo $?;
```




















