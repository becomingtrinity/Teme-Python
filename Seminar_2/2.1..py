my_list = list('ABcdEfghI')

i = 0
while i <= len(my_list):
    if my_list[i] > 'A' and 'Z' > my_list[i]:
        print(my_list[i])
    i += 1
    break
