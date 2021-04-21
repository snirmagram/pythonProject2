num=int(input("enter number: "))
def is_prime(n) :
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(13))

i=1
num= int(input("enter number:"))
for a in range(i,num):
    if num%a==0:
        print("true")
        break
else:
    print("false")