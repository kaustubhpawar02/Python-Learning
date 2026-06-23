def Area(radius,pi):
    ans = pi * radius * radius
    return ans


def main():
    ret = Area(pi=3.14, radius=10.5)
    print(" AREA OF CIRCLE IS :",ret)

if __name__ =="__main__":
    main()