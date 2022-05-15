from math import sqrt
n = 1
prime_indicator = 0

if (n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_indicator = 1
            break
    if (prime_indicator == 0):
        print(True)
    else:
        print(False)
else:
    print(False)
