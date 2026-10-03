# challenge 1
# accept the student's name and three subject marks and calculate and print the marks and name in one line

name = input("entre student's name: ")
la = float(input("entre the linear algebra marks: "))
boe = float(input("entre the basic of enggineering marks: "))
pfe = float(input("entre the proggraming of enggineering marks: "))

total_marks = la + boe + pfe

print(f"the student's name is {name} and have scored {total_marks} marks in three subjects")
