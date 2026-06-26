def Area(Radius , PI = 3.14):
    Ans = PI*Radius*Radius
    return Ans

def main():
    rad =float(input("Enter radius :"))
    ret = Area(rad)
    print("Area of circle is :", ret)

    ret = Area(12.5,7.5)
    print("Area of circle is :",ret)

if __name__ == "__main__":
    main()
