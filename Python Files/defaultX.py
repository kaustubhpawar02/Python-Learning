def Area(pi=3.14, radius):            #Error
    ans = pi * radius * radius
    return ans


def main():
    ret = Area(10.5)
    print(" AREA OF CIRCLE IS :",ret)

    ret = Area(10.5,7.12)
    print(" AREA OF CIRCLE IS :",ret)

if __name__ =="__main__":
    main()