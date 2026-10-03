# NAMED PARAMETERS
"""
 there are two named parameters which are optional
 end and sep(sepration)
 1) end parameter
 denoted by end='' or end=""
    what it does is that if there are two print funtion but we want it on 
    single line on the screen then we use it.
eg:-
    print("abc", end="")
    print("xyz")
what it does it that after printing abc it will end the line there itself and start a new line after it 
we can add diffrent symbols to in between "" to show the sepration between two prints

NOTE = defalt print("*object, end'\n'")
    the \n means that to strat the next print or funtion on new line of screen, but if remove that 
    from the print funtion like we did it in eg then insead of creating new line it will continue 
    on same line.


2) SEP(sepration) FUNTION
denoted by sep="" or sep=''
    what it does
        if we look at the #3rd sloution of space problem 
        print("hello,", name) ==> print("hello,", name, sep=" ")
        here both means the same thing, what sep=" " does is that to it tell python to give a space 
        after in the place of the comma which is a defalt thing
    but,
        we can do chance the space thing and add another symbol to it 
eg:- 
    print("hello,", name, sep="$$$")


"""

name = input("whats your name? ")

print("hello, ", end="")
print(name)

# if we add something in btween "" then,
print("hello, ", end="$$")
print(name)
# \n means new line but $$ means nothing so python just prints it on screen


print("hello,", name, sep="$$$")
