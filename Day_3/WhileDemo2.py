#Write a program to find the sum of the first N natural numbers using a while loop.

n = int(input("Enter a number : "))

sum = 0

x = 1

while(x<=n):
    sum = sum + x

    x = x + 1

print("The Sum of First",n,"Natural number is :",sum)
     



