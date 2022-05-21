# 6.2 Bash Startup Files

* bash shell 的启动状态可以有若干种特征。
  * **interactive shell** - interactive 状态下，bash 通过 terminal 完成输入输出。一般的 bash 命令行就是 interactive 的。而使用 bash -c 执行一段命令或者使用 bash 运行一个脚本时，一般而言就是 non-interactive 的。使用以下命令可以检查当前的 bash 是不是 interactive 的：
  * ```text
    [[ $- == *i* ]] && echo 'Interactive' || echo 'Not interactive'
    ```
  * login shell - 在 bash 运行时，如果 `$0` 参数的值是 `-bash` ，这个 bash 就是一个 login shell；在执行 bash 时带上 --login 参数也会得到一个 login shell（注意这样并不会使 `$0` 变成 `-bash`  ）。通过 ssh 远程登录时看到的 shell 就是 login shell 状态的，可以打印 `$0` 观察 。（但在使用一些图形界面或者其他终端登录时并不会得到 login shell）使用以下命令可以检查当前的 bash 是不是 login 的：
  * ```text
    shopt -q login_shell && echo 'Login shell' || echo 'Not login shell'
    ```
* 以下规则按优先级从高到低排列。
  * 当 bash 以 login shell 状态运行，bash 在启动时首先执行`/etc/profile` ，然后顺次检查 `~/.bash_profile`, `~/bash_login` ,`~/.profile` 并执行找到的第一个可执行的脚本。
    * 虽然不属于 startup 的范畴，不过还有一个特性：使用 exit 命令退出的时候，bash 会检查 `~/.bash_logout` 并在脚本存在时执行。
  * 当 bash 以 interactive non-login shell 状态运行，bash 在启动时检查 `~/.bashrc` 并在脚本存在时执行。使用 `--rcfile` 参数可以为 bash 提供一个替代的初始化文件。
    * 小知识：`bashrc` 是 `RUNCOM` ，进而是 `bash run commands` 的缩写。 
    * > It stands for “[run commands](http://en.wikipedia.org/wiki/Run_Commands)”.
      >
      > This comes from [MIT](http://en.wikipedia.org/wiki/MIT)’s [CTSS \(Compatible Time-Sharing System\)](http://en.wikipedia.org/wiki/Compatible_Time-Sharing_System) and [Multics](http://en.wikipedia.org/wiki/Multics), where the idea that a command processing shell would be an ordinary program originated. CTSS had a program called RUNCOM \(for “run commands”\) and a script was called “a runcom” in the community where Unix originated, leading to the file extension `.rc` and generally to the `rc` abbreviation.
      >
      > `rc` stuck as a name for any list of commands. \(by [Gilles 'SO- stop being evil'](https://superuser.com/users/42315/gilles-so-stop-being-evil) edited by [Scott](https://superuser.com/users/150988/scott)\)
  * 当 bash 以并非上述状态的 non-interactive shell 状态运行（例如只是执行一个脚本），bash 检查环境变量 `$BASH_ENV` 并把这个变量的值作为初始化文件的路径。
* 当 bash 通过 `sh` 命令调用，会采取类似 `sh` 的行为：
  * 当 bash 以 login shell 状态运行，bash 顺次检查 `/etc/profile` 和 `~/.profile` 并执行。
  * 当 bash 以 interactive shell 状态运行，bash 检查环境变量 `$ENV` 并把这个变量的值作为初始化文件的路径。
  * 当 bash 以并非上述状态的 non-interactive shell 状态运行，则不会读取任何 startup file。
* 其他还有一些调用 bash 的方式会导致不同的初始化行为，在此不展开。\( ref: \[4\] \)

## Reference

\[1\] [https://unix.stackexchange.com/questions/26676/how-to-check-if-a-shell-is-login-interactive-batch](https://unix.stackexchange.com/questions/26676/how-to-check-if-a-shell-is-login-interactive-batch)

\[2\] [https://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell/46856](https://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell/46856)

\[3\] [https://superuser.com/questions/173165/what-does-the-rc-in-bashrc-etc-mean](https://superuser.com/questions/173165/what-does-the-rc-in-bashrc-etc-mean)

\[4\] [https://www.gnu.org/software/bash/manual/html\_node/Bash-Startup-Files.html](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)

