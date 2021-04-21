str="shalom 123"
#    0123456789
#print(str[2])
#a

#if "sh" in str:
#    print("found")
#else:
#    print("not found")
#found

#for i in str:
#    print(i)
#s
#h
#a
#l
#o
#m

#1
#2
#3
#print(str[2:8])
#alom 1

#print(str[-3:])
#123

#print(len(str))
#print(max(str))
#print(max(str))

str="this is my first python lesson in my course"
#print("count s", str.count("s"))
#print("count my", str.count("my"))

#print("index s",str.index("S",5))

#print("find s",str.find("s"))
#find s 3
#print(str.isnumeric())
#False
#print(str.capitalize())
#This is my first python lesson in my course


#print(str.upper(), str.lower())
#THIS IS MY FIRST PYTHON LESSON IN MY COURSE
#this is my first python lesson in my course

#מחליף משהו מסויים באותיות גדולות
#print(str.replace("my","MY"))
#this is MY first python lesson in MY course

print(str)
str=input("enter number: ")
#מוריד את הרווחים ושם לי כל מילה בתא נפרד
list1=str.split()
#['this', 'is', 'my', 'first', 'python', 'lesson', 'in', 'my', 'course']

#להמיר לint
print(list1)
list2=[]
for i in list1:
    list2.append(int(i))
print(list2)
#יוצר רשימה חדשה
#[10, 20, 30, 40, 50]

#עוד דרך להמיר ל unt
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(list1)
#עוד דוגמא לאיך ליצור רשימה חדשה
#[10, 20, 30, 40, 50]
