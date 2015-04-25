##1.  下载网页版本电子书的好方法：  
wget镜像html版的电子书  
wget --mirror  -p --convert-links -p . http://interactivepython.org/courselib/static/pythonds/index.html


##2.  curl代理下载文件  
curl -x  proxy -o 文件名 下载地址