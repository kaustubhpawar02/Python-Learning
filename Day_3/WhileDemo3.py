#Write a program to display the multiplication table of a given number using a while loop.


N = int(input("Enter a Number : "))

Mult = 0

i = 1

print("Multiplication Table is :\n")

while(i*N <= N*10):

    Mult = Mult + N

    print(Mult)

    i = i + 1







