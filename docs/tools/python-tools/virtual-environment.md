# Virtual Environment

## 虚拟环境和依赖

```text
# 安装
pip install virtualenv
# 在当前路径下创建名为 env_name 的虚拟环境
virtualenv [--no-site-packages] [--python=2.7] env_name
--python 指定python版本（一般而言应该指定指向 python 解释器的路径）
--no-site-packages 不包含系统的 site-packages 即全局安装包
运行 source env_name\bin\activate 来激活虚拟环境，激活后：
(env_name) current_path$
运行 deactivate 关闭虚拟环境
​
管理工具：virtualenvwrapper
pip install virtualenvwrapper
pip install virtualenvwrapper-win (for windows)
​
安装后在~/.bashrc中写入
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh　
​
mkvirtualenv [--python=python_path] env_name #创建虚拟环境，可选指定python版本
workon #查看当前虚拟环境目录
​
```

