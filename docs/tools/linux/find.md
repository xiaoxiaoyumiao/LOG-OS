# find

* find 命令
  * -name &lt;pattern&gt; 提供待匹配的文件名 pattern
  * -regex &lt;pattern&gt; 使用 EMACS regex 语法匹配文件路径（注意不是文件名）
  * -maxdepth &lt;non-negative-number&gt; 控制搜索的最大深度
  * -mindepth &lt;non-negative-number&gt; 控制搜索的最小深度
  * -exec &lt;commands&gt; ; 对匹配到的每个文件执行 command
    * 执行时将 command 中的 {} 替换为当前匹配到的文件
    * exec 读入 command 内容时到分号为止
    * 为了防止被 shell 替换，一般把 {} 和 ; 保护起来，如 '{}' 和 \;
    * 一个能运作的例子：`find . -maxdepth 1 -name "*.lbl" -exec echo '{}' \;` 查找当前目录下所有后缀为 .lbl 的文件并打印文件名
  * man find 中的 OPERATORS 一节提供了参数级别的搜索条件运算
    * \(\) 可以提升运算的优先级，但要写成 \\( \\) 转义，且和其他参数之间以空格分隔
    * -a 以与关系连接两个搜索条件，当且仅当左侧条件满足时计算右侧条件
    * -o 以或关系连接两个搜索条件，当且仅当左侧条件不满足时计算右侧条件
    * 一个能运作的例子：`find . -maxdepth 1 \( -name '*.typ' -o -name '*.lbl' \) -exec echo '{}' \;` 查找当前目录下所有后缀为 .typ 或 .lbl 的文件并打印文件名

