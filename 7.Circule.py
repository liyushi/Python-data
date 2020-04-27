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
