# INTIGER OPRATONS

"""
+ -> addition
- -> subtration
* -> multiplication
/ -> division
% -> remiander (modulo oprator)
** -> power
int() -> converts str into intigers
float() -> converts str into intigers having decimal
round() -> round off the number 
"""

# ## calculator
# x = float(input("what's x? "))
# y = float(input("what's y? "))

# z = round(x + y)

# print(f"{z:,}") 
# # adds commas in the solutions

# """
# a = round(x / y, 2)
# """
# # ', 2' it does that it round off number to two decimal point

# # solution 2:
# a = x / y
# print(f"{a:.2f}") 
# # what ".2f" means is that to put decimal point in solution after two places
 

# return

def main():
    x = int(input("whats is x?: "))
    print("x squared is ", square(x))

def square(n):
    return(n*n)

main()