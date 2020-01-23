if __name__ == '__main__':
    # 绝对值
    print(abs(-100))
    # 最大值
    print(max(2, 3, 1, -5))
    # 数据转换
    print(int('123'))
    print(float('12.34'))
    print(str(1.23))
    print(bool(1))
    print(bool(''))

    # 可以将函数赋予一个变量 作为函数的引用
    ab = abs
    print(ab(-1))
    # 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
    n1 = 255
    n2 = 1000
    print(str(hex(n1)))
    print(str(hex(n2)))

    # 函数的定义 注释与定义间隔一行 如果函数执行完毕也没有return则自动return None

    def my_abs(x):
        # 参数检查
        if not isinstance(x, (int, float)):
            raise TypeError('参数类型错误')
        if x >= 0:
            return x
        else:
            return -x


    print('函数执行结果', my_abs(-10))

    # 空函数

    def nop():
        pass

    nop()

    # 返回多值 实际上返回的是一个tuple
    import math

    def move(x, y, step, angel=0):
        nx = x + step * math.cos(angel)
        ny = y - step * math.sin(angel)
        return nx, ny

    rx, ry = move(100, 100, 60, math.pi / 6)
    print(rx)
    print(ry)
    print(move(100, 100, 60, math.pi / 6))

    # 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解
    import math

    def quadratic(a, b, c):
        # 注意有很多条件
        # print(pow(b, 2) - 4 * a * c)
        # print(-b + math.sqrt(pow(b, 2) - 4 * a * c))
        return (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a), (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    # print(quadratic(1, 2, 3))
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')
