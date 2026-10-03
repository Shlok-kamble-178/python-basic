# complex data types

#lists
marks = [10, 20, 50, 5, "pyhsics", 65.454]

"""
10 is a 0th index here and 20 is the 1st index.
index is the element of the list. -1 is the use in
slicing of a list to tell last position of the list
and just like that -2 for 2nd last ans -3 for 3rd last
and so on. 
print(marks[:]) tells that to print the list for first to last
print(marks[4:]) from 4th index to end
print(marks[:-2]) form starting to 2nd last index
and print(marks[]) is use for indiviual index 
but need to tell position like 0,2,5 or -1,-2...

"""
print(marks, type(marks))
print(len(marks)) # lenght of list
#index
print(marks[0]) # 0th index   here, 10
print(marks[2]) #2nd index  here, 50
print(marks[-1])  # last index  here, 65.454
print(marks[-2])   # 2nd last index here, physics
# slicing a list -- list[st:end]
print(marks[:4]) 
print(marks[1:3])