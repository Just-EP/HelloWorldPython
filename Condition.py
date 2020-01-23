if __name__ == '__main__':
    age = 20
    if age >= 18:
        print('Your age is', age)
        print('adult')

    age = 3
    if age >= 18:
        print('Your age is', age)
        print('adult')
    else:
        print('your age is', age)
        print('teenager')
    age = 3
    if age >= 18:
        print('Your age is', age)
        print('adult')
    elif age >= 6:
        print('your age is', age)
        print('teenager')
    else:
        print('kids')
    # 当多个if条件时,一旦符合条件就会退出判断 后续代码不在执行

    # input
    s = input('请输入生日:')
    birth = int(s)
    if birth > 2000:
        print('你是00后')
    else:
        print('你不是00后')

    # 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    #
    # 低于18.5：过轻
    # 18.5-25：正常
    # 25-28：过重
    # 28-32：肥胖
    # 高于32：严重肥胖

    h = 1.75
    w = 80.5
    b = w / (pow(h, 2))
    print('小明的BMI', b)
    if b < 18.5:
        print('过轻')
    elif 18.5 <= b < 25:
        print('正常')
    elif 25 <= b < 28:
        print('过重')
    elif 28 <= b < 32:
        print('肥胖')
    else:
        print('严重肥胖')
