if __name__ == '__main__':
    # 递归
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n - 1)
    print(fact(10))
    # 尾递归的方式可以解决递归调用栈溢出问题
    # 尾递归指的是返回的应当是方法返回值本身 而不应包含计算

    def fact_iter(num, result):
        if num == 1:
            return result
        else:
            return fact_iter(num-1, num * result)
    print(fact_iter(10, 1))

    # 汉诺塔
    # move(n, a, b, c) 参数n表示三个柱子A,B,C中第一个柱子A的盘子数量 然后打印出所有盘子从A借助B移动到C的方法
    # 根据n的数量进行判断
    # 如果n的数量为3 将A->B n-1
    # 如果n的数量为2 A->C
    def move(n, a, b, c):
        if n == 1:
            print(a, '->', c)
        else:
            move(n - 1, a, c, b)
            print(a, '->', c)
            move(n - 1, b, a, c)
    move(3, 'A', 'B', 'C')
