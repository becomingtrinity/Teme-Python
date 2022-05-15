numbers =[12, 5, 3.8, 1000, 374, 612.3, 921.9, 52, 71, 68]
print(min(numbers))
print(max(numbers))

the_minimal_number =float("inf")
the_maximal_number =float("-inf")
for e in numbers:
    if e > the_maximal_number:
        the_maximal_number = e
    if e < the_minimal_number:
        the_minimal_number = e
        print("Your minimal number is: ", the_minimal_number)
        print("Your maximal number is: ", the_maximal_number)