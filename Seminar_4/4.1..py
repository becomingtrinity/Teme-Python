def prim(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False

        return True
number = int(input("The number is: "))
if prim(number):
    print("Is prime number")
else:
    print("Isn't prime number")