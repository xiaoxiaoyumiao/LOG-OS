# Miscellaneous

* Why do we use %% before temp variables in a batch file?( ref: \[1] )
* In a batch file, the following parsing process is carried out before script execution:
  * %1, %2, ..., %9 are interpreted into command line parameters;
  * %0 is replaced by the command used to execute the batch file;
  * single % is replaced by null;
  * A pattern like %VAR%(VAR can be any string) is replaced by corresponding environment variable with name VAR. If VAR doesn't exist, the pattern is replaced by null.
  * %% is interpreted into %.
* where：类似 linux 中的 which 工具
  * `where.exe python` 会给出 python 的位置。
  * .exe 是必要的。
* 关于变量声明和使用
  * 使用 `$VariableName = VariableValue` 来以值 `VariableValue` 创建名为 `VariableName` 的变量。
  * 同样使用 `$VariableName` 来取得该变量的值。
  * 与 bash 不同，PS 中的字符串值需要用引号括起。例如 `$Greeting = "Hello World"` 。
  * `$null` 表示空值。
* 关于逻辑运算符
  * 基本的逻辑判断运算符为 `-eq` , `-ne` , `-gt` , `-lt` , `-le` , `-ge` （相等，不等，大于，小于，不大于，不小于）。表达式是中缀的，即 `a -eq b` 表示 a 与 b 做相等运算。`-and`, `-or`, `-xor`, `-not`, `!` 则用于布尔值的运算。
* 关于执行多条命令
  * 使用分号分隔即可以在同一行内书写多条命令。
  * ref: [https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell](https://superuser.com/questions/612409/how-do-i-run-multiple-commands-on-one-line-in-powershell)

## Reference

[\[1\] Q75634: Percent Signs Stripped from Batch File Text](https://jeffpar.github.io/kbarchive/kb/075/Q75634/)

[\[2\] What is Windows' equivalent of the “which” command in Unix? Is there an equivalent PowerShell command?](https://superuser.com/questions/207707/what-is-windows-equivalent-of-the-which-command-in-unix-is-there-an-equivale)

\[3] [https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about\_variables?view=powershell-7.2](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about\_variables?view=powershell-7.2)

