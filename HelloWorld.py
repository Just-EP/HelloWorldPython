# -*- coding: utf-8 -*-
# 注释
if __name__ == '__main__':
    string = "Hello World"
    print(string[0:-1])
    print(string[0])
    print(string[2:5])
    print(string[2:])
    print(string * 2)
    print(string + "你好")

    import sys;x = "Hello";sys.stdout.write(x+"\n")

    x = "a"
    y = "b"
    print(x)
    print(y)
    print(x, end="")
    print(y, end="")

    import sys
    print('================Python import mode==========================')
    print('命令行参数为:')
    for i in sys.argv:
        print(i)
    print('\n python 路径为', sys.path)

    from sys import argv, path
    print('================python from import===================================')
    print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
    print("Hello", "World")
    name = input("Please input your name:")
    print("Hello", name)
