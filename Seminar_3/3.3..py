chemical_processes = ["dissolvation","acidification", "pH"]
chemical_processes.reverse()
print("Your reversed list is:", chemical_processes)

r = []
for e in chemical_processes[::-1]:
    r.append(e[::-1])
    print("Your mirrored elements list is:", r)