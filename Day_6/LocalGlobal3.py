no = 11 

def Display():
    no = 21            # only accessible in display
    print("From Display :",no)

print("Before :",no)  #11
Display()             #21
print("After :",no)   #11