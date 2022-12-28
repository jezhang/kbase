
## ffmpeg 处理 http/https 文件时报 Segmentation fault (core dumped) 错误

ffmpeg 为 https://johnvansickle.com/ffmpeg 上下载的预编译程序，在处理 http/https 应用时报了  Segmentation fault (core dumped) 错误。

经多番查找在 stack overflow 上找到相关贴子: 

<https://stackoverflow.com/questions/60528501/ffmpeg-segmentation-fault-with-network-stream-source>

 

总结如下:

在 ffmpeg  的网站上，有构建说明， https://johnvansickle.com/ffmpeg/release-readme.txt 

里面提到：

    Notesa:  A limitation of statically linking glibc is the loss of DNS resolution. Installing nscd through your package manager will fix this.

    The vmaf filter needs external files to work- see model/000-README.TXT

就是说 ffmpeg 的 DNS 解析需要 nscd 这个服务才能正常。

所以解决方案有这么几个：

1. 安装并启动 nscd 服务。

```sh
apt install nscd
systemctl enable nscd
systemctl start nscd
```
2. 将 http/https 的 URL 自己手动把其中的域名部分替换成 IP 地址。(对于我来说并不适用于此

3. 将 http/https 的资源转为本地资源，比如如果是 OSS 的文件的话，可以尝试使用 ossutil 把 OSS bucket 挂载到云主机上