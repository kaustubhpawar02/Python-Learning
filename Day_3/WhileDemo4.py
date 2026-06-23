#Write a program to count the number of digits in a given integer using a while loop.

num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

print("Number of digits:", count)



