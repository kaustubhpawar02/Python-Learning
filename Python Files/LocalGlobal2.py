no = 11            # Global Variable

def Display():
    a = 21

    print("from display :",no)

    print("From display value of a is :",a)    #local variable

def Demo():
    #print("from demo value of a :",a)   # error
    print("from display :",no)

Display()

Demo()