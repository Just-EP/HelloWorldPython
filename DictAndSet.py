if __name__ == '__main__':
    # dict 相当于其他语言中的map 使用key-value存储
    d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Micheal'])
    # 通过key放入元素
    d['Adam'] = 67
    print(d)
    d['Jack'] = 90
    print(d)
    d['Jack'] = 88
    print(d)
    # 取不存在的key会报错
    # 使用in关键字判断key在dict中是否存在
    print('Thomas是否在dict中', 'Thomas' in d)
    # 使用dict的get()方法
    print('如果Thomas不存在返回None', d.get('Thomas'))
    print('如果Thomas不存在也可指定返回数值', d.get('Thomas', -1))
    # 移除一个元素
    d.pop('Bob')
    print('在d中移除Bob', d)
    # 关于dict
    # dict顺序与放入顺序无关
    # 查询和插入速度快 不收数量影响 占用内存高
    # key必须是不可变对象

    # set 一组key集合 不能重复 类似Java中的Set
    s = {1, 2, 3}
    print(s)
    # 与顺序无关 只是指定set中有哪些元素
    s = {3, 2, 1}
    print(s)
    # 不重复
    s = {1, 2, 2, 3, 4, 4, 5}
    print(s)
    # 添加删除元素
    s.add(6)
    print(s)
    s.remove(4)
    print(s)
    # set可以做数学意义上的交集 并集操作
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print('交集:', s1 & s2)
    print('并集:', s1 | s2)

    t = (1, 2, 3)
    d = {t}
    print(d)
    # tuple是不可变对象,当内部元素都是不可变时,才能放入dict或set中
    # t = (1, [2, 3])
    # d = {t}
    # print(d)
