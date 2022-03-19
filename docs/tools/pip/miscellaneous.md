# Miscellaneous

* 关于换源
  * [https://blog.csdn.net/yuzaipiaofei/article/details/80891108](https://blog.csdn.net/yuzaipiaofei/article/details/80891108)
* 似乎推荐的调用方法还是 python -m pip ... （或者 python3 -m pip）
* -f / --find-links &lt;url&gt;
  * 指定一个包含安装包（.tar.gz 或 .wheel）的路径。pip 会在该路径下搜索指定的安装包。
  * 在 ubuntu 服务器上安装某个巨大的包的时候，因为根目录空间不足导致甚至无法下载安装包本身，所以先把相应版本的 .whl 下载到本地，然后通过 ssh 上传到服务器的磁盘空间，再使用 -f 命令指向存放 .whl 文件的本地路径。
  * 追加：更加科学的方法是重新设置缓存目录，方法为在命令前添加 TMPDIR=&lt;dir&gt; 或者 export TMPDIR=&lt;dir&gt; ，也就是改变环境变量 TMPDIR的值，其中 dir 为希望设置的缓存目录。

## Reference

\[1\] [https://pip.pypa.io/en/stable/reference/pip\_install/](https://pip.pypa.io/en/stable/reference/pip_install/)

\[2\] [https://stackoverflow.com/questions/40755610/ioerror-errno-28-no-space-left-on-device-while-installing-tensorflow](https://stackoverflow.com/questions/40755610/ioerror-errno-28-no-space-left-on-device-while-installing-tensorflow)

