if __name__ == '__main__':
    # 获取list前三个元素
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[0:3])
    # 切片中0可省略
    print(L[:3])
    # 负数表示倒数索引
    print(L[-2:-1])

    # 创建0-99的list
    L = list(range(100))
    print(L[:10])
    print(L[-10:])
    # 前10个数每两个取1个
    print(L[:10:2])
    # 所有数每5个取1个
    print(L[::5])
    # 复制list
    print(L[:])

    # tuple同理

    # str操作
    print('ABCDEFG'[:3])
    print('ABCDEFG'[::2])

    # 利用切片操作实现trim()函数

    print(' a '.strip())

    def trim(s):
        if s != '':
            while s[0] == ' ':
                s = s[1:]
                if s == '':
                    return s
            while s[-1] == ' ':
                s = s[:-1]
                if s == '':
                    return s
            return s
        else:
            return s
    st = '   ABCD '
    print(trim(st))
    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
