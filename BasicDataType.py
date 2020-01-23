# -*- coding: utf-8 -*-
if __name__ == '__main__':
    counter = 100  # 整数
    miles = 1000.0  # 浮点数
    miles2 = 1.23e12  # 科学计数法
    str1 = "Hello"  # 字符串 在python中 单引号和双引号都可以作为字符串的表示方式
    str2 = 'World'
    str3 = "I'm OK"
    str4 = 'I\'m "OK"'
    str5 = "I'm \"OK\""

    print(counter)
    print(miles)
    print(str4)
    print(str5)
    # python 变量赋值方式
    a = b = c = 1
    d, e, f, = 1, 2, "HelloWorld"
    # python 判断变量类型
    print(isinstance(counter, int))
    print(isinstance(miles, float))

    print(miles2)
    # python允许使用 r''表示 ''内的字符串不进行转义
    print('\\\t\\')
    print(r'\\\t\\')
    # 在交互命令行中 python允许使用'''...'''表示多行内容
    print('''line1
... line2
... line3''')

    # 布尔值
    true = True
    false = False
    print(true and false)
    print(true and true)
    print(false and false)

    print(true or false)
    print(not true)

    # age = input('请输入年龄')
    age = 19
    if age >= 18:
        print('adult')
    else:
        print('teenager')
    # 空值
    n = None
    # 动态语言 变量可在不同数据类型之间相互切换
    g = 123
    print(g)
    g = 'ABC'
    print(g)
    '''
    python解释器在内存中创建字符串'ABC'
    创建一个g变量,指向'ABC'
    '''
    h = 'ABC'
    i = h
    h = 'XYZ'
    print('最终h的值为:', h)
    print('最终i的值为:', i)

    # 常量 在python中常量使用大写的变量名表示 但事实上仍然是变量
    PI = 3.14
    # python除法
    # /表示浮点除法
    print(10/3)
    print(9/3)
    # 整除除法
    print(10//3)
    print(9//3)
    # 练习
    print('------练习-------')
    print(123)
    print(456.789)
    print("'Hello, world'")
    print("'Hello, \\'Adam\\''")
    print("r'Hello, \"Bart\"'")
    print("r'''Hello,\nLisa!'''")

    print(1/3)


