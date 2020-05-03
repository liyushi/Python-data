def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input('m='))
n = int(input('n='))
print(fac(m)//fac(n)//fac(m-n))

from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
print(add(c=50,a=100,b=200))
'''
1.设置默认值，如果调用函数的时候没有传入对应参数的值，将使用该参数的默认值
2.与其他语言的函数重载的效果是一致的
'''


