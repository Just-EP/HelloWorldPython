if __name__ == '__main__':
    # filter()用于过滤序列 返回值为一个Iterator
    def is_odd(n):
        return n % 2 == 1
    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

    # 删除一个序列中的空串
    def not_empty(s):
        return s and s.strip()
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

    # 用filter求素数

    # 先构造一个3开始的奇数序列
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n
    max = 100
    for n in _odd_iter():
        if n < 100:
            print(n)
        else:
            exit()
    # 筛选函数
    # def _not_divisible(n)