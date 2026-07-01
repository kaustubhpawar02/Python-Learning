no = 11       # Global Variable

def Display():

    a = 21      # Local variable
    print("From Display :",no)
    print("from display value of a is :",a)

def Demo():

    #print("From demo value of a is ",a)    # Error a is access only in display fun
    print("from demo :",no)

Display()
Demo()