def summation(data):

    Sum = 0

    for no in data:
        Sum = Sum + no

    return Sum


def main():
    Marks = [78,90,56,98,77]

    ret = summation(Marks)
  
    print("Addition is :",ret)


if __name__ == "__main__":
    main()