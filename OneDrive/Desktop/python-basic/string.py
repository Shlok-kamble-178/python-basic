name = "shlok kamble"
grade = "A"

#string operations
print(name.upper())
print(name.lower())

#Find
print(name.find("f")) # -1 means not found
print(name.find("k")) # 6 means found at index 6

#replace
print(name.replace("shlok", "shlok shekhar"))
print(name.replace("shlok", "shlok shekhar").upper())

#check the presence
print("shlok" in name) # True
print("i" in name) # False