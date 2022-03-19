# Virtual Environment

## Dependency

### Human

* [Virtual Environment](../../tools/python-tools/virtual-environment.md)

## Setup, Use & Delete

```bash
# create a virtual environment with name <env_name>
conda create --name <env_name>
conda create -n <env_name>

# specify python version:
conda create -n <env_name> python=<version>
```

使用 `conda activate <env_name>` 激活这个虚拟环境。使用 `conda deactivate` 退出当前激活的虚拟环境。

与 `virtualenv` 不同，conda 并不默认在本地创建虚拟环境的文件夹。使用 `conda info --envs` 查看当前安装的所有包，例如：

```bash
conda info --envs
.../Anaconda3
.../Anaconda3/envs/env
```

删除一个虚拟环境可以使用的命令：

```bash
conda env remove --name <env_name>
conda remove --name <env_name> --all
```

使用 `--prefix` 指定虚拟环境文件夹路径。例如：

```text
conda create --prefix ./envs
```

这个虚拟环境需要通过路径指定激活：

```text
conda activate ./env
```

## Work with Pip

如果已经有了一个 conda 虚拟环境，但 conda install 能安装的包并不太齐全，而想用 pip 安装，可以考虑：

```text
conda install pip
pip install -r requirements.txt
```

安装时注意自己调用的是不是虚拟环境里的 pip。

## Environment Variables

```text
conda env config vars set my_var=value
```

使用以上命令可以在当前虚拟环境中设置环境变量，它可以在虚拟环境启动时自动设置。首次设置后需要重启虚拟环境生效。

## Reference

\[1\] [https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

\[2\] [https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment](https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment)

\[3\] [https://blog.csdn.net/robot8me/article/details/109471568](https://blog.csdn.net/robot8me/article/details/109471568)

