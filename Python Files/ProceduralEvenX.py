def CheckEven(no):
    if (no%2==0):
        return True

    else:
        return False

def main():
    value = int(input("enter a number :"))

    ret = CheckEven(value)

    if(ret == True):
        print("even")

    else:
        print("odd")

if __name__ == "__main__":
    main()