# opening a file in python. modes: w = write, r = read, a = append, r+ = read+write
"""

f = open("sample.txt","w")      #(filename, mode) creates a new file if file does not exist
f.write("Hello world")
f.close()       # close a file



# Using with (Best practise to open a file)
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)  # by using with we don't need to close file it automatically closes


with open("sample.txt", "r") as f:
    print(f.read())
    f.seek(0)   #moves cursor back
    

    print(f.readline())   #print one line
    print(f.readlines())    #list of all lines

"""

# Writing and appending
 

 #write (overwrite file)

"""
with open("sample.txt", "w") as f:
    f.write("First line\n")

with open("sample.txt", "a") as f:
    f.write("This is anoter line\n")

with open("sample.txt", "r") as f:
    print(f.read())
    print(f.readline())   #print one line
    print(f.readlines()) 

"""

# Working with CSV files:
"""
import csv

#writing

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Aditya","24"])

#Reading

with open("data.csv", "r", ) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

"""

# Exerice 1: create a file notes.txt and store 3 lines in it.
"""
with open("notes.text","a") as f:
    f.write("This is 1st line\n")
    f.write("This is 2nd line\n")
    f.write("This is 3rd line")

with open("notes.text","r") as f:
    print(f.read())

with open("notes.text","w") as f:
    pass    #wipes out file data
"""
# Exercise 2: Write a program that reads notes.txt and print each line with line number


    