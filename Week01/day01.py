# Week 1 Day 1: Variables, Data Types, Expressions

name = "Alex"
age = 34
height = 5.9
is_learning_ml = True

print(f"My name is {name}, I'm {age} years old, {height} feet tall.")
print(f"Currently learning ML: {is_learning_ml}")

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_ml))

x = 10
y = 3

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} ** {y} = {x ** y}")

num_str = "42"
num_int = int(num_str) + 10
print(f"Converted '{num_str}' to int and added 10: {num_int}")