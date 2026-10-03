# inventing our own funtions

# def -> define
# return -> to return an value

#to="world" means that if we doesn't write anyting inside hello()
# then the defalt word world will be print 
# like end and sep in the print funtion(optional parameters) 
def hello(to="world"):
    print("hello,", to)

hello()


name = input("whats your name? ").title()
hello(name)

"""
not everytime we can define the funtion on the top, so, what we will do is that 

we will define another funtion. let, it called main (and lets solve above problem again with this method)
    def main():
        name = input("whats your name?")
        hello(name)
    
    def hello(to="world"):
        print("hello,", to)

    main()

what will this do is that, as program runs form top to bottom and left to right
so fist we define main as a fuction and run the task but we haven't define hello funtion so it will give no output
then as the program run forwad it will find that hello funtion is define. and what main() will do is that the program
will revisit main funtion to complete the funtion. and will give a output 
        
"""
def main():
        name = input("whats your name?").title()
        hello(name)
    
def hello(to="world"):
        print("hello,", to)

main()

# look at int.py for return example