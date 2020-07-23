#!/usr/bin/python3
"""
filename = "file.txt"
# 1. 打开文件
f = open(filename, 'w')
# 2. 对文件操作
f.write("hello python1 hello westos")
# 3. 关闭文件
f.close()
"""
"""
filename = "file.txt"
# 1. 打开文件
f = open(filename, 'r')
# 2. 对文件操作
content = f.read()
print("文件的内容: ", content)
# 3. 关闭文件
f.close()
"""


filename = "file.txt"
# 1. 打开文件
f = open(filename, 'a+')
# 2. 对文件操作
f.write("\nhello python2 hello westos")
# 3. 关闭文件
f.close()
