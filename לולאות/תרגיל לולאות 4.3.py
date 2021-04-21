import random as rnd
num1=int(input("enter number"))
num2=rnd.randint(1, 9)
print(("num2"))
while num1 != num2:
    if num1 > num2:
        print("the number you inserted is a bigger")
        num1 = int(input("insert a new number"))
    else:
        print("the number you inserted is smaller")
        num1= int(input("insert a mew number"))
print("the numbers are equal")