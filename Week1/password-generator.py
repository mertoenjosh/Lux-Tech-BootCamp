def factorial(x):
    if x==0:
        return 1
    else:
        return factorial(x-1) * x

print ("This is a simple program to find factorial of a number")
try:
    num=int(input("Please enter a number to calculate factorial\n(num)> "))
except:
    print("Enter an integer")

mystring = "{} factorial is {}"
print(mystring.format(num, factorial(num)))
