def Calculation(no1,no2):
    Mult = no1*no2
    Div = no1/no2
    return Mult ,Div
    

def main():
    value1 = int(input("Enter Value 1 : "))

    value2 = int(input("Enter Value 2 :"))

    res1 , res2 = Calculation(value1,value2)

    print("Multiplication is :",res1)
    print("Division is :",res2)

if __name__ == "__main__":
    main()