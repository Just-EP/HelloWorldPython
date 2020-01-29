if __name__ == '__main__':
    # 变量可以指向函数
    print(abs)
    # abs(-10)是函数调用 而abs是函数本身
    # 可以把函数赋值给变量
    f = abs
    print(f)
    # 可调用
    print(f(-10))
    # 函数名也是指向函数的变量

    # 传入函数 变量可以指向函数 那么函数参数可以接收变量 被称为高阶函数

    def add(x, y, func):
        return func(x) + func(y)
    a = -5
    b = 6
    print(add(a, b, abs))

    # map() 接收两个参数 一个是函数 一个是Iterable
    # 函数 f(x) = x*2 把这个函数作用在一个list[1, 2, 3, 4, 5, 6, 7, 8, 9]上

    def f(x):
        return x * x
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(r)
    print(list(r))

    # 将上述list中的元素全部转换为字符串
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

    # reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上 必须接收两个参数
    # reduce把结果继续和序列的下一个元素做累计计算 reduce(f, [x1, x2, x3. x4]) = f(f(f(x1, x2), x3), x4)
    # 对一个序列求和
    from functools import reduce

    def add(x, y):
        return x + y
    print(reduce(add, [1, 3, 5, 7, 9]))

    # 将序列[1, 3, 5, 7, 9] 转换为 13579
    def fn(x, y):
        return x * 10 + y
    print(reduce(fn, [1, 3, 5, 7, 9]))

    # 将str转换为int的函数

    from functools import reduce

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    reduce(fn, map(char2num, '13579'))

    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # lambda函数简化

    def char2num(s):
        return DIGITS[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    # 利用map() 将用户输入的英文转换为首字母大写 其他字母小写的形式

    def normalize(name):
        return name[0].upper() + name[1:].lower()

    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    def m(x1, x2):
        return x1 * x2

    def prod(L):
        return reduce(m, L)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    def char2float(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def str2float(s):
        i = s.index('.')
        l = len(s)-1
        s = s.replace('.', '')
        return reduce(fn, map(char2float, s))/pow(10, l - i)

    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
