#Data Structures(Lists, Tuples, sets, dictionaries)

#Lists (ordered, changeable) can be changed
"""
list = ["hello", "hola", "hi", "bonjour", 14]
print(list[0:4:2])   #[start, stop, gap]
list.append(5) 
print((list))


#Tuples (ordered, unchangeable) cannot be changed

coordinates = (10, 20 , "hello", 4.13)
print(coordinates[0])

#sets (unordered, unique items) useful for membership checks:

number = {1,2,3,3,4,4,5,6}
print(number)
print(3 in number)  # return True if 3 is in numbers



#Dictioneries (key -value pairs)

student = {
    "Name" : "Aditya",
    "City" : "Lucknow",
    "Age" : 24
}

student["Age"] = 25         # updation

for key, value in student.items():
    print(key, ":", value)


#Exercise 1 : Create a list of 5 no and print sum, min, max

list = [12, 15, 85, 25, 4]
print(sum(list))
print(max(list))
print(min(list))


#Exercise 2 : Create a tuple of 5 friends name and try to change one of those

name = ("John", "Cat", "Liz", "Alex", "Ramu")
name[1] = "frank" 



#Exercise 3 : Write a program to remove duplicates from lists using sets

list1 = [1,2,2,3,4,4,5,6,6]
print(list(set(list1)))



#Exercise 4 : create a diction of 3 students with name, age and score

students = {
    "student1": {"name": "Aarav", "age": 20, "score": 85},
    "student2": {"name": "Neha", "age": 22, "score": 90},
    "student3": {"name": "Kabir", "age": 21, "score": 78}
}

print(students["student1"])

"""

#Exercise 5 : Write a program that counts how many times a word appers in a string

def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

text = "python is fun and python is easy"
print(word_count(text))
"""
