"""
PRINT and INPUT FUNTIONS 

print("abc!")
    its a print funtion, it gives output whatever is inside the parentheses '()' 
    - used to show information on screen

input("absd")
    its a input fuction, it store the string given by user 
    - used to collect information

both are use to at a time to collect and show info

but to store more data efficently we need to assine specific characters to unique data or info
eg:-
    for name
    name = input("whats your name?")
    it will store the info in a string called 'name'
    to print it 
    print(name)
"""

# eg:- 
name = input("whats your name? ")
print("hello," + name)
# this program collect the info(name of user) and print it on the screen
#       but there is a problem that it has no space after comma 
# solution:-
print("hello,"+ " " + name)  #1st
print("hello, " + name) #2nd
print("hello,", name) #3rd the best way
print(f"hello, {name}") #4th
# in 4th solution f means format i.e format string


# problem 2: if we want quotation"" marks on the screen
# solution : use diffrent quotion marks or use \ before quatations
print("hello, 'friend'") # or
print('hello, "friend"')
print("hello, \"friend\"") 