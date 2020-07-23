#!/usr/bin/python3
try_count=0
while try_count < 3:
    print("**************login system***************")
    name = input("Name")
    passwd = input("Passwd")
    if name == "root" and passwd == "123":
        print("login success")
        break
    try_count += 1
    print("login%d" %(try_count))
else:
    print("login too much time")
