import math
class1 = int(input("Enter number of students in class 1: "))
class2 = int(input("Enter number of students in class 2: "))
class3 = int(input("Enter number of students in class 3: "))

total_students = class1 + class2 + class3

total_desks = math.ceil(total_students/2)

print(f"The minimum number of desk required are {total_desks} ")
