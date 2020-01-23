if __name__ == '__main__':

    # 可定义必选参数 默认参数 可变参数和关键字参数

    # 位置参数 改造
    # def power(x):
    #     return x * x

    def power(x, n):
        r = 1
        while n > 0:
            n = n - 1
            r = r * x
        return r

    print(power(5, 3))
    print(power(5, 4))

    # 默认参数

    def power(x, n=2):
        r = 1
        while n > 0:
            n = n - 1
            r = r * x
        return r
    print(power(5))

    # 注意 必选参数在前 默认参数在后
    # 当函数有多个参数时 把变化大的参数放在前面 变化小的参数放在后面 变化小的可作为默认参数
    # 这样做降低了函数调用的难度 因为当参数填写不全时 默认从前向后匹配参数

    def enroll(name, gender):
        print(name)
        print(gender)

    enroll('Sarah', 'F')

    def enroll(name, gender, age=6, city='Beijing'):
        print('name:', name)
        print('gender:', gender)
        print('age:', age)
        print('city:', city)

    enroll('Sarah', 'F')
    # 可以不按顺序提供参数 这样要调用时要加上参数名称
    enroll('Adam', 'M', city='Tianjin')
    # 坑

    def add_end(L=[]):
        L.append('END')
        return L
    print(add_end([1, 2, 3]))
    print(add_end())
    print(add_end())

    # 默认函数需要指向不变的对象
    def add_end(shit=None):
        if shit is None:
            shit = []
        shit.append('END')
        return shit

    print(add_end())
    print(add_end())

    # 可变参数
    def calc(number):
        sum = 0
        for n in number:
            sum = sum + n * n
        return sum

    print(calc([1, 2, 3]))
    print(calc([1, 3, 5, 7]))
    # 变成可变参数

    def calc(*number):
        sum = 0
        for n in number:
            sum = sum + n * n
        return sum

    print(calc(1, 2))
    print(calc())

    # 可将list或tuple转换为可变参数
    nums = [1, 2, 3]
    print(calc(*nums))

    # 关键字参数 允许传入0个或任意个含参数名的参数 这些关键字能够自动组装成dict

    def person(name, age, **kv):
        print('name:', name, 'age:', age, 'other', kv)
    person('Micheal', 30)
    # 关键字参数 city = 'Beijing'
    person('Micheal', 30, city='Beijing')
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Micheal', 30, city=extra['city'], job=extra['job'])
    # 简化 **extra会获得extra的拷贝 对其进行修改不会影响extra内容
    person('Micheal', 30, **extra)

    # 命名关键字参数 关键字参数对参数key没有限制 可以使用命名关键字参数限制关键字参数的key值

    # * 符号后的为命名关键字参数 命名关键字必须传入参数名 否则调用将报错

    def person(name, age, *, city, job):
        print(name, age, city, job)
    person('Jack', 24, city='Beijing', job='Engineer')

    # 命名关键字参数同样可以设定缺省值
    def person(name, age, *, city='Beijing', job):
        print(name, age, city, job)
    person('Jack', 24, job='Engineer')
    # 如果不加*分隔符会被认为是位置参数

    # 参数组合
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    t = ['a', 'b']
    f1(1, 2, 3, *['a', 'b'])
    f1(1, 2, 3, *t)
    f1(1, 2, 3, *t, x=99)
    ex = {'x': 99}
    f1(1, 2, 3, *t, **ex)

    args = (1, 2, 3, 4)
    kw = {'d': 88, 'x': '#'}
    # 对于任何函数都可以使用如下方式调用
    f1(*args, **kw)
