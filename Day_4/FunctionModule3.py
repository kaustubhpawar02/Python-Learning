from Marvellous import Addition

def main():

    value1 = int(input("Enter first number :"))

    value2 = int(input("Enter second number :"))

    ret = Addition(value1,value2)

    print("Addition is :",ret)

    # ret = Subtraction(value1,value2)   #Error
    # print("Substraction is : ",ret)
    
if __name__ == "__main__":
    main()