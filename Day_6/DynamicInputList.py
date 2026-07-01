def main():
    Arr = []

    print("enter number of elements")
    Size = int(input())
    print("Enter elements :")
    for i in range(Size):
        no = int(input())
        Arr.append(no)
    print(Arr)

    print("Addition of Above elements in list is :")
    sum = 0
    for i in Arr:
        sum = sum + i
    print(sum)

if __name__ == "__main__":
    main()

    