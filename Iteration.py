if __name__ == '__main__':
    # 迭代遍历dict
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)

    for value in d.values():
        print(value)
    for k, v in d.items():
        print('key:', k, 'value:', v)

    # 字符串迭代
    for ch in 'ABC':
        print(ch)

    # 判断一个对象是否为可迭代
    from collections.abc import Iterable
    print(isinstance('abc', Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance(123, Iterable))
    # enumerate函数将list变为索引-元素的形式
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    # 同时引用两个变量
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

    # 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

    def find_min_and_max(L):
        max = None
        min = None
        for a in L:
            if max is None or a > max:
                max = a
            if min is None or a < min:
                min = a
        return min, max
    # 测试
    if find_min_and_max([]) != (None, None):
        print('测试失败!')
    elif find_min_and_max([7]) != (7, 7):
        print('测试失败!')
    elif find_min_and_max([7, 1]) != (1, 7):
        print('测试失败!')
    elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

