# creating a simple finction
"""
def hello():
    print("Hello this is a finction")     

hello()     # calling a function:

"""
"""
def greet(name):
    print(f"hello {name}, welcome to our group!")

greet("Aditya")
"""

"""
*args -- multiple positional arguments
*kwargs -- multiple keyword arguments

def add(*args):
    return sum(args)

print(add(1, 2, 4, 5, 6))
"""
"""
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
details(name="Aditya", age= "24", city = "Lucknow")
"""
"""
#Exercise 1 : write a function is_even(n), that return true id n is even and false if not

def is_even(n):
    print( n%2 == 0)

i = int(input("Enter a number: "))
is_even(i)

"""

# Exercise 3 : Write a function factorial(n) that returns factorial of n
'''
def factorial(n):
    count = 1
    while n>0:
        count = count*n
        n = n-1
    return count

print(factorial(5))

'''
'''

#Exercise 4: Write a function reverse_string() to reverse string

def reverse_string(string):
    return string[::-1]     #reverse string

print(reverse_string("hello world"))

'''

'''
#Exercise 5: rite a function calculator(a, b, op) where op can be add, sub, mul, div

def calculator(a ,b, op):
    if op == "sum":
        n = a+b
    elif op == "sub":
        n = a-b
    elif op == "mul":
        n = a*b
    elif op == "div":
        n = a/b
    return n

print(calculator(5,3,"sum"))

'''
#Exercise 5: write a function fibonacci(n), that prints fibonacci of first n numbers

def fibonacci(n):
    a=0
    b=1
    for _ in range(n):
        print(a, end = " ")
        a, b=b, a+b

fibonacci(5)