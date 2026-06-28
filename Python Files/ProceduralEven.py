def CheckEven(no):
    if (no%2==0):
        print("its even no")

    else:
        print("its odd no")

def main():
    value = int(input("enter a number :"))

    CheckEven(value)

if __name__ == "__main__":
    main()