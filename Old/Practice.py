for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

'''
水仙花数
'''
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)


for x in range(0,20):
    for y in range(0,33):
        z = 100-x-y
        if 5*x+3*y+z/3==100:
            print('公鸡:%d,母鸡:%d,小鸡:%d'%(x,y,z))
'''


'''
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')
'''


''' 
FirstNum = 1
SecondNum = 1
x = int(input('请输入要输出的斐波那契数量'))
for i in range(x):
    FirstNum, SecondNum = SecondNum, FirstNum + SecondNum
    print(FirstNum,SecondNum)

# Function for nth Fibonacci number

def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))

#This code is contributed by Saket Modi
'''
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
'''
斐波那契数列
'''