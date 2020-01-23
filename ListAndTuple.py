if __name__ == '__main__':
    # list 有序集合,可以随时添加和删除其中的元素
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    # 元素个数
    print(len(classmates))
    # 可以使用索引访问list中每一个位置中的元素
    print('第一个元素:', classmates[0])
    print('最后一个元素:', classmates[len(classmates) - 1])
    # 若索引为负数 可获取倒数索引位置的元素
    # 倒数第3个元素
    print('倒数第三个元素:', classmates[-2])
    # 添加元素
    classmates.append('Adam')
    print('新集合:', classmates)
    # 插入到指定索引位置
    classmates.insert(1, 'Jack')
    print('插入指定位置: ', classmates)
    # 删除末尾元素
    classmates.pop()
    print('删除末尾:', classmates)
    # 删除指定位置
    e = classmates.pop(1)
    print('删除第二个:', classmates)
    print('删除的元素:', e)
    # 替换某个位置的元素
    classmates[1] = 'Sarah'
    print('替换第二个元素:', classmates)
    # list内的数据类型不一定相同
    L = ['Apple', 123, True]
    print('元素类型不同:', L)
    # list嵌套
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print('计算外层元素数量', len(s))
    print('取集合内集合的数据:', s[2][1])
    # 空集合
    L = []
    len(L)
    print('空集合', L)
    print('空集合长度:', len(L))

    # 元组 不可变 在不需要改变数据的情况下推荐使用元组
    classmates = ('Michael', 'Bob', 'Tracy')
    # 只可以读取元组数据
    print('第二个元组数据:', classmates[1])
    # 元组必须在定义时确定元素
    t = (1, 3)
    print('定义元组:', t)
    t = ()
    print('空元组', t)
    # 元组歧义问题
    # t = (1) 这种单元素元组写法与小括号存在歧义, 在python中规定这种写法归为数字
    # 定义元组需要在元素后加, 以消除歧义
    t = (1,)
    print(t)
    # 元组元素的不变指的是指向不变
    t = ('a', 'b', ['A', 'B'])
    print('改变前:', t)
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print('改变后:', t)

    # 请用索引取出下面list的指定元素：
    L = [['Apple', 'Google', 'Microsoft'],
         ['Java', 'Python', 'Ruby', 'PHP'],
         ['Adam', 'Bart', 'Lisa']]
    print(L[0][0])
    print(L[1][1])
    print(L[2][2])
