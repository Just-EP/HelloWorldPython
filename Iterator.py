if __name__ == '__main__':
    # 迭代器
    # 可以直接用for循环的数据类型有以下几种
    # 1 集合数据类型 list tuple dict set str等
    # 2 generator 包括生成器与带yield的generator function
    # 这些统称为可迭代对象Iterable 可使用isinstance()判断
    from collections.abc import Iterable

    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance('abc', Iterable))
    print(isinstance((x for x in range(10)), Iterable))
    print(isinstance(100, Iterable))

    from collections.abc import Iterator

    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance([], Iterator))

    # 可使用iter()函数将Iterable转换为Iterator
    print(isinstance(iter([]), Iterator))

    # Python的for循环本质上就是通过不断调用next()函数实现的，例如：

    for x in [1, 2, 3, 4, 5]:
        print(x)

    # 等价于
    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
