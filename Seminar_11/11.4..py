import os
start_directory = 'D:\Python labs'
total_space_occupied = 0
for root, directories, files in os.walk(start_directory):
    for file in files:
        total_space_occupied += os.stat(f'{root}/{file}').st_size
print('Path:', start_directory)
print('Space occupied:', total_space_occupied)