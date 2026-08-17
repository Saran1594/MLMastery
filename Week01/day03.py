# Nested Loops Multiplication table Example
for i in range(1,5):
    for j in range(1,13):
        print(f"{i}*{j}={i * j}")
# Star program
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()
