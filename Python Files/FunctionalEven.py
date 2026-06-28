CheckEven = lambda no : (no%2==0)
   
    

def main():
    value = int(input("enter a number :"))

    ret = CheckEven(value)     # ret = (value%2==0)

    if(ret == True):
        print("even")

    else:
        print("odd")

if __name__ == "__main__":
    main()
