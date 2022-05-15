import os
nr_documents = nr_directories = 0
start_directory = 'E:\Thievery Corporation Discography'
for root, directories, documents in os.walk(start_directory):
    nr_directories += len(directories)
    nr_documents += len(documents)

print('Path:', start_directory)
print(f'Nr. dirs:', nr_directories)
print(f'Nr. files:', nr_documents)
