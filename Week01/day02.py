# Day 2 is all about loops
# if plus if else loop
for i in range(7):
    if i > 5:
        print(f"{i} is greater than 5")
    elif i < 5:
        print(f"{i} is lessthan than 5")
    else:
        print(f"{i}")
# While loop
x = 10
while x < 5:
    print(f"{x} is greater than 5")
    x = x + 1
#for loop with break and continue
for i in range(5):
    if i != 5:
        break
    if i % 2 == 0:
        continue
    print(i)