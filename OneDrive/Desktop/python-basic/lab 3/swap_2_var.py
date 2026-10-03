a = int(input("enter a: "))
b = int(input("enter b: "))
temp = a
a = b
b = temp
print(f"value of a: {a}")
print(f"value of b: {b}")

print(f"after swapping: a = {a} and b = {b}")

"""
here, we created a temparary variable temp and we assign the value of a in it 
then a become empty so then we assign value of b in a and temp in b 
"""
