# File System & I/O

## System

文件路径都是字符串，用/分割或者\转义

os模块：

```python
os.getcwd() #返回当前工作路径
os.chdir(path) #改变路径，参数是一个字符串
os.remove(filename)#删除给定文件名的文件，参数是一个字符串
os.rmdir(dirname)#删除一个目录，参数是字符串
os.mkdir(dirname)#创建一个一层目录，参数是字符串
os.makedirs(path)#创建一个多层目录，参数是字符串
​
os.path.split(dirnameAndFilename) #把文件路径的目录和文件名分割，返回字符串二元组(dir,name)
os.path.abspath(curPath) #获得绝对路径
os.path.splitext(filename) #获得文件扩展名(dir_name,ext)（如("a",".jpg")）
​
os.path.isdir(path) #判断目录是否存在（或者说判断path是否是一个目录）
os.path.isfile(path) #判断文件是否存在
os.path.exists(path) #判断路径是否存在
​
os.path.join(path, file) # 拼接得到适合OS的路径
​
time.ctime(os.path.getatime(file))
time.ctime(os.path.getmtime(file))
time.ctime(os.path.getctime(file))
```

可采用os.walk\(\)和os.listdir\(\)两种方法，遍历指定文件夹下的文件。

os.walk\(\)

```python
for root, dirs, files in os.walk(".", topdown=False):
    #...
```

模块os中的walk\(\)函数可以（递归地）遍历文件夹下所有的文件（包括目录和非目录）。

os.walk\(top, topdown=True, onerror=None, followlinks=False\) 该函数可以得到一个形如\(dirpath, dirnames, filenames\)的三元tupple构成的列表。

* dirpath：string，代表路径top下的一个子路径（一个子目录）；
* dirnames：list，包含了路径dirpath下所有的子目录名字（不包含目录路径）；
* filenames：list，包含了路径dirpath下所有的非目录子文件的名字（不包含目录路径）

os.listdir\(path\) 只遍历 path 一层目录下的文件而不进入子目录。

sys模块：

```python
#sys.argv可以获取运行环境参数，[0]是被运行的脚本路径
sys.exit()
sys.hexversion#获取解释程序的版本值
#其他还可以获得最大INT，最大UNICODE，操作系统平台等等
__console__ = sys.stdout #stdout指定标准输出
sys.stdout = somefile
print('something')#被输入到some file中
```

shutil模块

```python
shutil.move(full_path, despath)
shutil.copyfile(full_path, despath)
```

## std I/O

```python
# 常用的 end 参数，设置打印的结尾，默认为换行符
print(data, end='')
```

## File I/O

```python
fileHandler = open(name[, mode[, buffering]])#filehandler是一个文件File对象
```

* name : 一个包含了你要访问的文件名称的字符串值。
* mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读\(r\)。w为从头写入并在不存在时创建新文件，a为追加并在不存在时创建新文件，
* buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

```python
# 读取文件内容， size_number 为可选的读入字节数上限
file.read(size_number)
# 返回一行
file.readline()
# 一次性读入文件全部内容，返回size行构成的列表
file.readlines([size])
for line in f:
    somefunc(line)#可以迭代
f.write('string')
# writelines 虽然叫这个名字，但实际上是不在元素间插入换行符的
# 以下命令会把 str1str2 打印到文件
f.writelines(['str1', 'str2'])
f.close()
```

### 文件IO之指针定位

seek\(offset, from\)

offset ：文件指针偏移量

from ：偏移计算类型， 0-从文件开头往后推 1-当前位置往后推 2-文件末尾往前推

对于汉字（utf-8），offset==3才算偏移了一个汉字。

调用一次fin.read\(\)之后，指针就移动到了全文末尾。（如果调用一次fin.seek\(0\)就又会回到开头）

这里注意用‘r'打开的文件是只能使用模式0的，用'r+'或者’rb‘打开成二进制文件才可以使用012.

但这时候需要合适的进行解码）

```python
with open("xxxx.txt", "r", encoding= "utf-8") as f:
    print(f.read())    # helloworld
    f.seek(8)
    print(f.read())    # rld
```

