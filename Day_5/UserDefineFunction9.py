def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlor")

    Amul()      #Allowed
    Amul()      #Allowed

def main():
    BigBazar()     #Allowed

if __name__ == "__main__":
    main()