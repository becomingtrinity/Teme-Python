import os

def size_capacity(py):
    if os.path.isfile(py):
        return os.path.getsize(py)
    else:
        size = 0
        for file in os.listdir(py):
            size += size_capacity(os.path.join(py, file))
        return size

get_directory = 'D:\Python labs'
print('The path of directory is:', get_directory)
print('The size of all directory files is:', size_capacity(get_directory))