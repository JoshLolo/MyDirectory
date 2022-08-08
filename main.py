# MyDirectory
# August 2022
# Josh Lolo
# CIS245
# Script to create a file of users choice

# /home/runner/MyDirectory
# This was to take note of what directory I was in
import os

os.mkdir('testbed1')
os.mkdir('testbed2')
#os.chdir('test')
#print(os.getcwd())
# I could have also used os.mkdir(and ask for user input instead)
while True:
  directory = input("Would you like to use testbed1 or testbed2: ")
  if not os.path.isdir(directory):
    print("You did not enter testbed1 or testbed2")
  else:
    #print("You are here") This is a test line to see what happened
    break
os.chdir(directory)
#print(os.getcwd())
# I used this statement to make sure I was in the proper directory

file_name = input("What is the name of your file: ")

with open(file_name, 'w') as fileHandle:
 name = input("What is your name: ")
 fileHandle.write(name + ",")
 address = input("What is your address: ")
 fileHandle.write(address + ",")
 phone_number = input("what is your phone number: ")
 fileHandle.write(phone_number + ",")
  
#print(f"The directory you chose is {directory}, the file name you chose is {file_name}.\nYour name is {name}, your address is {address}, your phone number is {phone_number}")
# Testing output options
p = open(file_name, 'r')
contents = p.read()
print(contents)
p.close
