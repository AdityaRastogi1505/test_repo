# comprehenions let you creae lists, sets and dictionaries in a single line, instead of writing long loops. They make code cleaner and faster

#list comprehension for squares of numbers
"""
squares = [i*i for i in range(5)]
print(squares)

#sets comprehension remainder.

nums = {i%3 for i in range(10)}
print(nums)

# Dictionary Comprehensions

square= {i : i*i for i in range(5)}
print(square)
#Nested Comprehensions

matrix = [[i for i in range(3)] for j in range(3)]
print(matrix)



#Exercise 1: Create a list of all odd number between 1 to 20

odd = [i for i in range(20) if i%2!=0]
print(odd)

"""

"""
#Exercis 2: Given words = ["pyhton", "is", "fun"], create a list of their length
words = ["pyhton", "is", "fun"]
len = [len(word) for word in words]
print(len)



# Exercise 3: create a dictionary that maps no 1 to 5 to their cubes

cube = {i: i**3 for i in range(6)}
print(cube)



#Exercise 4: given a sentence, create a list of all unique vowels used in it.
vowel = ["a","i","e","o","u"]
text = "Hello this is a sentence"

count = { i for i in text if i in vowel}
print(count)

"""

#Exercise 5 : Flatten a 2D list [[1,2],[3,4],[5,6]] into a single list using comprehension

list1 = [[1,2],[3,4],[5,6]]
flatten = [i for j in list1 for i in j]

print(flatten)
