if __name__ == '__main__':
    # for in 循环 用于循环list或tuple
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum+x
    print(sum)
    # range()函数 生成一个整数序列 list()函数 将序列转化为list
    print(list(range(101)))
    sum = 0
    for x in range(101):
        sum = sum+x
    print('1-100的和为:', sum)

    # while 循环 满足条件时执行循环 不满足条件时退出循环
    # 100以内奇数和
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    # 请利用循环依次对list中的每个名字打印出Hello, xxx!：
    L = ['Bart', 'Lisa', 'Adam']
    for name in L:
        print('Hello, %s!' % name)
    # break 退出循环
    n = 1
    while n <= 100:
        print(n)
        n = n + 1
    print('END')

    n = 1
    while n <= 100:
        if n > 10:
            break
        print(n)
        n = n + 1
    print('END')
    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0:
            continue
        print(n)
