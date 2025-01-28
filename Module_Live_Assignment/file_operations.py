
# Module with functions for reading, writing, and appending data to a file.

def fopen(path, mode):
    file = open(path, mode)
    return file

def fclose(file):
    file.close()

def fread(file):
    return (file.read())

def fwrite(file, st):
    file.write(st)
