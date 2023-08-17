#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

sum_result = add(2, 3)

def halve(number):
    if not isinstance(number, (int, float)):
        return 'halve two'
    return number / 2

result1 = halve(4)
result2 = halve("not NO")

greet_programmer()
greet("Guido")
greet_with_default("Guido")
greet_with_default()

print(sum_result)
print(result1)
print(result2)