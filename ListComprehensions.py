if __name__ == '__main__':
    print(list(range(1, 11)))
    # 列表生成器
    for x in range(1, 11):
        print(x)
    # 使用列表生成器生成 1-10 x*x 列表
    var = [x * x for x in range(1, 11)]
    print(var)
    # for循环后加上if判断 可筛选出仅偶数的平方
    var = [x * x for x in range(1, 11) if x % 2 == 0]
    print(var)
    # 实现全排列
    var = [m + n for m in 'ABC' for n in 'XYZ']
    print(var)
    # 列出当前目录下所有文件和目录名
    import os

    var = [d for d in os.listdir('.')]
    print(var)
    # 使用列表生成器将dict转换为list
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    var = [k + '=' + v for k, v in d.items()]
    print(var)
    # 转换小写
    L = ['Hello', 'World', 'IBM', 'Apple']
    var = [s.lower() for s in L]
    print(var)
    # 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
    # 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
    L = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L if isinstance(s, str)]
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
