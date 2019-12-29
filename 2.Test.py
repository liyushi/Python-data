F = input("The number enter:")
while F != 1:
    if F%2 == 0:
        print("{}/2={}".format(F,F//2))
        F//=2
    else:
        print("{}*3+1={}".format(F,3*F+1))
        F=3*F+1
