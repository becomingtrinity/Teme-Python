import os
nr_files = 0
start_directory = 'D:\Python labs'
for root, directories, files in os.walk(start_directory):
    for file in files:
        if file.lower().split('.')[-1] == 'py':
            nr_files += 1
            print(f'{root}/{file}')

print('Nr. python files:', nr_files)