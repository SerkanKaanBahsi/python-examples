import os

# Get current directory
print(os.getcwd())

# print(os.getcwdb()) bu sorun yaratıyor
# change directory
# os.chdir()
print("hey")

# List directories and files
print(os.listdir())

# Making a new Directory
# we can give a path or it creates right here
# os.mkdir("Deneme")
print(os.listdir())

# Renaming a Directory
# os.rename("Deneme","Test2")
print(os.listdir())

# Removig a Directory
os.rmdir("Test2")

# os.rmdir("Test") #only works on empty directories
# os.remove() boş ise silmiyor
print(os.listdir())

# We can use this to remove a non empty directory
# import shutil
# shutil.rmtree()
