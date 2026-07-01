def Summation(Data):
    Sum = 0
    for i in Data:
        Sum  = Sum + i
    return Sum
    

def main():

    Arr = list()

    print("Enter number of elements :")
    Size = int(input())

    print("Enter elements :")

    for i in range(Size):
        values = int(input())
        Arr.append(values)
    print(Arr)
    
    print("After Doing Addition of all elements in array :\n")

    res = Summation(Arr)

    print("Addition is :",res)

if __name__ == "__main__":
    main()