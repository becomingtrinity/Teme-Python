import os

def initial_folder(py):
    if os.path.isfile(py):
        if py.lower().split('.')[-1] == 'py':
            print(py)

        else:
            for file in os.listdir(py):
                initial_folder(os.path.join(py, file))

start_directory = 'D:\Python labs'
initial_folder(start_directory)