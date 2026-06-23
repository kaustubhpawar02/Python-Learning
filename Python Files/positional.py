def Area(radius,pi):
    ans = pi * radius * radius
    return ans


def main():
    ret = Area(10.5,3.14)
    print(" AREA OF CIRCLE IS :",ret)

    ret = Area(13.6,7.12)
    print(" AREA OF CIRCLE IS :",ret)



if __name__ =="__main__":
    main()