# CHAPTER 1


# learning how to take input from user
name = input("Enter your name?: ")
print("Hello, " + name) # concatination of string

# or we can write it aslo as
print("hello,", name)
# here in this code we don't need to give extra space as comma is already giving a space

# END
# 1) end is a optional parameters of print function which prints the end 'value' like 
# print("hello,", end="")
# print(name)
# what will this code will do is that it will end the 14th line as 'hello,' and will contiue with 
# 15th line "name" a string
# if insead of just end="" if we written end="!!!" we would have gotten 
#                                                         hello,!!!name     as an output
print("hello,", end="")
print(name)

# SEP
# 2) now the sep(sepration) is a aslo optional parameter of print
# after comma(,) we get a defalt space but we could print anything if we want insead of that space
# print("hello,", name, sep="888")
# as an output we would get hello,888name
print("hello,", name, sep="@@")