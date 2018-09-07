
将Linux终端会话录制成SVG动画
==========================

<https://www.ostechnix.com/how-to-record-terminal-sessions-as-svg-animations-in-linux/>


## Installing Termtosvg

Termtosvg can be installed using PIP, a python package manager to install applications written using Python language. If you haven’t installed PIP already, refer the following guide.

```sh
pip3 install --user termtosvg
pip3 install pyte python-xlib svgwrite
```
Done. Let us go ahead and generate Terminal sessions in SVG format.

## Record Terminal Sessions As SVG Animations In Linux

Recording Terminal sessions using Termtosvg is very simple. Just open your Terminal window and run the following command to start recording it.

```sh
termtosvg
```

You will see the following output after running ‘termtosvg’ command:

```sh
Recording started, enter "exit" command or Control-D to end
```

You will now be in a sub-shell where you can execute the Linux commands as usual. Everything you do in the Terminal will be recorded.

Let me run a random commands.


```sh
$ mkdir mydirectory
$ cd mydirectory/
$ touch file.txt
$ cd ..
$ uname -a
```

Once you’re done, press CTRL+D or type exit to stop recording. The resulting recording will be saved in /tmp folder with a unique name.

You can then open the SVG file in any web browser of your choice from Terminal like below.

```sh
$ firefox /tmp/termtosvg_ddkehjpu.svg
```

You can also directly open the SVG file from browser (File -> <path-to-svg>).

Here is the output of the above recording in my Firefox browser.

![demo](http://www.ostechnix.com/wp-content/uploads/2018/08/Termtosvg-in-browser.gif)