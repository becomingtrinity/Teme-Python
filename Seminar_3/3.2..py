n = 9
factorial = 1

if n < 0:
    print("Your number that you've introduced is not available")
elif n == 0:
    print("The factorial number that you have introduced is: ")
else:
    for i in range(1,n + 1):
        factorial = factorial * 1
    print(f"The factorial number of", n,"is", factorial)