import random
def saikoro():
    return random.randint(1,6)

print("What is your name ?")
name = input()
print("Hello, " + name)
d1 = saikoro()
d2 = saikoro()
print("Rolling the dice...\nDie 1: %d\nDie 2: %d\nTotal value: %d" % (d1, d2, d1+d2))
if(d1 + d2 > 7):
    print("you won!")
else:
    print("you lost!")
