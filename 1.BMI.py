print("Please enter the weight and the height, must the order")
weight,height = eval(input())
BMI = weight/(height*height)
print("Your BMI is {0:.1f}".format(BMI))
if BMI < 18.5:
    print("too thin")
elif BMI < 24:
    print("normal")
elif BMI < 28:
    print("overweighht")
else:
    print("fat")

for F in range(0,301,20):
    c = 5/9 *(F-32)
    print("{} F={:.0f}c".format(F,c))
