'''
sum = 0
for x in range(2,101,2):
    sum += x
print(sum)

'''

'''

import random
answer = random.randint(1,1000)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print("Big more")
    elif number > answer:
        print('Small more')
    else:
        print('Bingo')
        break
print('Total %d ' % counter)
if counter > 7:
    print('foolish')
'''
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()
'''
'''
from math import sqrt
num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end + 1):
    if num % x == 0:
        is_prime = False
        break
    if is_prime and num != 1:
        print('%d是素数'%num)
    else:
        print('%d不是素数'%num)
'''

'''
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break


'''
row = int(input('请输入行数: '))
for i in range(row):
    for j in range(i + 1):
        print('*',end='')
    print()
'''

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
'''
'''
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
'''

'''


'''
里面一些代码还是不是很清楚
'''