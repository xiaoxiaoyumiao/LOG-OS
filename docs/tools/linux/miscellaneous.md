# Miscellaneous

* oneko
  * 可以在桌面生成一只会追逐鼠标的猫。
* man &lt;command&gt;
  * 查看 command 的 manual。在查询各个工具的作用和参数时非常有用。
  * 发挥类似作用的工具有 help 和 tldr，不过没有使用过。
  * man 的输出使用了 less 分页，其众多操作方法和 vim 类同。
    * 例如，使用 /&lt;pattern&gt; 搜索一个 pattern，并使用 n 和 N 向后或向前查找各个结果。
    * ref: [https://superuser.com/questions/304065/how-do-i-search-for-a-word-or-a-phrase-in-the-linux-man-command-and-cycle-thro](https://superuser.com/questions/304065/how-do-i-search-for-a-word-or-a-phrase-in-the-linux-man-command-and-cycle-thro)
* source / .
  * source &lt;file&gt;
  * source 将一个脚本加载到当前进程中执行。
  * [https://stackoverflow.com/questions/13786499/what-is-the-difference-between-using-sh-and-source](https://stackoverflow.com/questions/13786499/what-is-the-difference-between-using-sh-and-source)
* which &lt;command&gt;
  * 查看 command 实际执行了位于何处的程序。
* df 
  * 查看分区总空间和剩余空间。加上 -h 可以将数目换算为 K，M 等易于阅读的单位。
  * df \[path\] 可以查看 path 的空间使用情况
* kill &lt;pid&gt; 
  * 终止一个进程号为 pid 的进程
* top
  * 查看进程和 cpu 的使用情况（类似任务管理器）
* 关于环境变量定义
  * TODO 请检查这是否应该移动到 [Bash](../../programming-languages/bash/) section。
  * [https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)
  * [https://blog.csdn.net/qq\_32863631/article/details/76348963](https://blog.csdn.net/qq_32863631/article/details/76348963)
* nvidia-smi 显示显卡信息
  * CUDA version 指示驱动 API 版本，查看 CUDA toolkit 版本使用 cat /usr/local/cuda/version.txt
  * nvidia-smi -l \[second\] 命令可以每 \[second\] 秒（loop）打印一次显卡信息
  * [https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi](https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi)
  * [https://docs.nvidia.com/cuda/cuda-runtime-api/driver-vs-runtime-api.html](https://docs.nvidia.com/cuda/cuda-runtime-api/driver-vs-runtime-api.html)
  * [https://blog.csdn.net/sinat\_26871259/article/details/82684582](https://blog.csdn.net/sinat_26871259/article/details/82684582)
* 方便的目录栈：dirs, pushd, popd
  * [https://www.linuxprobe.com/linux-change-dir.html](https://www.linuxprobe.com/linux-change-dir.html)
* tail：快速浏览文件内容
  * 一般而言可以使用 tail 查看文件结尾的一段内容
  * tail -f（follow）参数可以将一个文件中追加写入的内容实时输出
  * ref：[https://www.cnblogs.com/fps2tao/p/8535519.html](https://www.cnblogs.com/fps2tao/p/8535519.html)
* `cd -` cd to the previous working directory
* kill - by default it uses `SIGTERM` = 15, but this may get ignored by some process (stuck in IO, for example). In this case try `kill -9` where 9 is `SIGKILL`. ref: https://askubuntu.com/questions/59811/kill-pid-not-really-killing-the-process-why; also check manual of `kill`
