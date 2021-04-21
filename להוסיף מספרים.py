list1=[]
#ככה מייצרים רשימה
for i in range(7):
    num=int(input("enter numer: "))
    list1.append(num)
print(list1)


num= int(input("enter number to delete"))

list2=list1.copy()

#[10,20,40,10,40,40,50]

#להוריד מספר ספציפי
for i in range(list1.count(num)):
    list1.remove(num)

print(list2)
print(list1)