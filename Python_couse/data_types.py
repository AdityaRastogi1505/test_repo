x = 10   #integer
y = 10.34   #float
z = "hello" #string
a = True    #Bool
b = False   #bool

#Type of variables

print(type(x))
print(type(y))
print(type(z))
print(type(a))

#Operator

print(x+y)  #addition
print(x-y)  #substraction
print(x*y)  #multiplication
print(x/y)  #division
print(x//y) #floor division
print(x%y)  #modulus
print(x**y) #exponent

#Comparision (returns bool value)   use ctrl+alt+ up or down arrow to multi edit

print(x==y)
print(x!=y)
print(x<y)
print(x>y)

#logical

print(a and b)
print(a or b)
print(not a)

# user input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"hello {name}, you are {age} years old!!")      #use of f-string 