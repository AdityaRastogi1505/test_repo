# if else statements
"""
age = 20
if age >= 18:
    print("you are an adult.")
else:
    print("your are a minor")
"""

#if-elif-else ladder
"""

marks = 40
if marks >=90:
    print("Grade: A")
elif marks >=75:
    print("Grade: B")
elif marks >=50:
    print("Grade: C")
else:
    print("Fail")

"""

#for loops
'''
for i in range(5):
    print("iteration, ", i, end= "\t")

'''

#while loop

'''
count = 1

while count <= 5:
    print("count:", count)
    count += 1
'''

# Break and continue
'''

for i in range(1,10):
    if i == 5:
        break   #stops loop
    print (i)

for i in range(1,10):
    if i%2 == 0:
        continue    #skip iteration
    print(i)

'''

# Exercise 1 
"""
write a program that print no till 20 but print fizz if multiple of 3, pirnt buzz
if multiple of 5 and priint fizzbuzz if multiple of both

for i in range(1,21):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

"""

#Exercise 2

""" take a no input n and print all even no upto n"""
"""

n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2 == 0:
        print(i)

"""

# Exercise 3

""" Write a program that ask for 5 no from user and print largest from it"""

a = []
for i in range(5):
    n = int(input("Enter a number: "))
    a.append(n)
print("The largest number is :", max(a))
    


# Exercise 4

""" make a secret no and ask user to input a no till he guess correct"""
"""
secret = 7
no = int(input("Enter a number: "))
while no != secret:
    no = int(input("You guessed wrong,try again! : "))
print("Congrats!!, You guessed it right.6")

"""