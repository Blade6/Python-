# -*- coding:utf-8 -*-
import os
print os.name
# posix -- Linux/Unix/Mac OS X
# nt -- Windows

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print os.path.abspath('.')

# 把两个路径合成一个时，不要直接拼字符串，
# 而要通过 os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数

# os.path.splitext()可以直接让你得到文件扩展名

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

# 你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 比如我们要列出当前目录下的所有目录，只需要一行代码：
print [x for x in os.listdir('.') if os.path.isdir(x)]
# ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Adlm', 'Applications', 'Desktop', ...]

# 要列出所有的.py文件，也只需一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']