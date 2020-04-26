"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: 骆昊
占位符 理解不到位
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (b, a, a + b))
print('%d - %d = %d' % (b, a, a - b))
print('%d * %d = %d' % (b, a, a * b))
print('%d / %d = %f' % (b, a, a / b))
print('%d // %d = %d' % (b, a, a // b))
print('%d %% %d = %d' % (b, a, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
第三行如何处理呢 不理解
"""
f = float(input('请输入华氏温度：'))
c = (f-32) /1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)