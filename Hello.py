print("Please enter the weight and the height, must the order")
weight,height = eval(input())
BMI = weight/(height*height)
if BMI < 18.5:
    print("Your BMI is"+ BMI)
    print("too thin")
elif 18.5 < BMI < 23.9:
    print("Your BMI is"+ BMI)
    print("normal")
elif 24 < BMI < 27.9:
     print("Your BMI is"+ BMI)
     print("overweight")
elif BMI>28:
    print("Your BMI is" + BMI)
    print("fat")


what ? false

emmm