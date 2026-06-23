def Calculation(No1,No2):
    Mult = No1 * No2
    Div = No1/No2
    return Mult,Div

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter first number : "))

    ret1 ,ret2 = Calculation(value1,value2)

    print("multiplication is :",ret1)
    print("division is : ",ret2)
    

if __name__ == "__main__":
    main()