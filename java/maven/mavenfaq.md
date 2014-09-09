Maven常见问题
=============

##如何在Eclipse里面添加M2_REPO classpath变量##

正常地，当你运行```mvn eclipse:eclipse```把Java项目转换成Eclipse Java项目，Maven会使用**M2_REPO**变量建好所有依赖和classpath。

**M2_REPO**只是一个Eclipse里面正常的"**classpath变量**"用来查找你本地Maven仓库。

我们演示2种方法添加**M2_REPO** classpath变量添加到Eclipse中。

###1.手动添加M2_REPO###
1. 依次打开Eclipse > Window > Preferences
2. 选择 Java > Build Path > Classpath Variables
3. 点击"New..."按钮 > 定义一个新 **M2_REPO**变量并且指向到你的本地Maven仓库
4. 完成
###2.自动添加M2_REPO - eclipse:configure-workspace###
```sh
mvn -Declipse.workspace="your Eclipse Workspace path" eclipse:configure-workspace
```
例子：
```sh
C:\>mvn -Declipse.workspace="C:\Users\woodchat\workspace" eclipse:configure-workspace
[INFO] Scanning for projects...
[INFO] Searching repository for plugin with prefix: 'eclipse'.
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Default Project
[INFO]    task-segment: [eclipse:configure-workspace] (aggregator-style)
[INFO] ------------------------------------------------------------------------
[INFO] [eclipse:configure-workspace {execution: default-cli}]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1 second
[INFO] Finished at: Thu Apr 14 20:45:17 SGT 2011
[INFO] Final Memory: 9M/112M
[INFO] ------------------------------------------------------------------------
```
完成


