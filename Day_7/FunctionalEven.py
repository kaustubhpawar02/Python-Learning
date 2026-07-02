is_even = lambda x : (x % 2 == 0)

def main():

    value = int(input("Enter a number :"))

    Ret = is_even(value)    # Ret = (value % 2 == 0)

    if(Ret == True):
        print("Its Even Number ")
    else :
        print("Its Odd number")

if __name__ == "__main__":
    main()