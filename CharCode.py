# ！/usr/bin/env python3
# 告知linux/os x系统 这是一个python可执行程序
# -*- coding: utf-8 -*-
# 告知python解释器 按照怎样的编码规范对源代码进行读取
if __name__ == '__main__':
    print('中文')
    # 获取字符的整数表示编码
    print(ord('A'))
    print(ord('中'))
    # 将编码转换为字符
    print(chr(66))
    print(chr(25991))
    # 字符串str
    x = 'ABC'
    # 字节类型 bytes 在字符串前加上b
    y = b'ABC'
    # 字符串调用encode方法将字符串转换为对应编码的char
    z = '中文'
    print(x.encode('ascii'))
    print(z.encode('utf-8'))
    # 读取流文件的数据为bytes 使用decode方法将其转换为str
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    # 中文转换ascii会报错
    # 字节长度不同会报错
    # print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('GBK'))

    # 计算字符个数
    print(len('ABC'))
    print(len('中文'))
    # 如果是bytes类型,则计算的是字节的个数
    print(len(b'ABC'))
    print(len('中文'.encode('utf-8')))

    # 格式化
    print('Hello,%s' % 'World')
    print('Hi, %s, you have $%d.' % ('xiaoming', 1))

    # 格式化 format() 方法 通过{0} ,{1}等占位符的方式
    # {1:.1f} {占位符:.保留位数f}
    print('Hello,{0},成绩提升了{1:.1f}%'.format('小明', 12))
    # 格式化整数和浮点数可以指定是否补0和整数与小数的位数
    print('保留小数位数', '%.2f' % 3.1415926)
    print('保留两个占位符位置,保留两个占位符并补0', '%2d-%02d' % (3, 1))
    print('保留两个占位符位置,保留两个占位符并补0', '%2d-%02d' % (13, 1))
    # 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
    s1 = 72
    s2 = 85
    r = ((s2 - s1) / s1) * 100
    s = ('%.1f' % r)
    print(r)
    print('小明的成绩提升了{0:.1f}%'.format(r))
    print(s)
