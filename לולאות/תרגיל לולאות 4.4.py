from random import randint
system_guess=randint (0,100)
print("system_guess")
answer=input("low or high or right?")
h1=100
l1=0
counter=0
while answer!="right":
    if answer=="high":
        h1 = system_guess - 1

    if system_guess=="low":
        l1=system_guess+1
        system_guess = randint(l1,h1)
    print(system_guess)
    answer = input("low oe high or right?")

print("good job")
