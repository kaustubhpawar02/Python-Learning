def main():
    Marks = [11,21,51,100]

    for no in Marks:
        print(no)

    Marks[2] =34

    print("-"*15)

    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()