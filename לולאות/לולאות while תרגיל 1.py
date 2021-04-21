num=int(input("enter num: "))

while 100<=num<=1000:
    if num >= 100:
        print("passed")
    else:
        print("failed")
    num = int(input("enter grade: "))

print("invalid grade. program ended.")
