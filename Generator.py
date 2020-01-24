if __name__ == '__main__':
    # 边循环边计算的机制成为生成器 将列表生成式的[] 改成 ()
    L = [x * x for x in range(10)]
    print(L)
    g = (x * x for x in range(10))
    # 使用next()方法调用生成器打印下一个元素
    print(next(g))
    print(next(g))
    print(next(g))
    # 如果统计到最后一个元素 没有更多的元素时 会抛出StopIteration异常
    # generator是可迭代对象 会保留状态
    print('--------')
    for n in g:
        print(n)

    # 斐波那契数列
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a+b
            n = n + 1
        return 'done'
    fib(10)

    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a+b
            n = n + 1
        return 'done'
    print(fib(10))

    # generator与函数执行流程不同
    # 函数是顺序执行 遇到return或最后一个语句退出
    # generator 每次调用next时执行 遇到yield返回 再次执行时 从上一个yield开始 到再次遇到yield结束

    def odd():
        print('step1')
        yield 1
        print('step2')
        yield 2
        print('step3')
        yield 5
    o = odd()
    print(next(o))
    print(next(o))
    print(next(o))

    for n in fib(6):
        print(n)
    # 只能获取yield返回的值 而不能获取return的值 想获取return的值 需要捕获StopIteration错误 返回值包含在StopIteration的value中
