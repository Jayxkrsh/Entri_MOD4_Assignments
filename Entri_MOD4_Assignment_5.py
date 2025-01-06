"""Write a Python program to read a file and display its contents"""
# file1=open("C:\\Users\\jayak\\Desktop\\filehand.txt",'r')
# print(file1.read())

"""Write a Python program to copy the contents of one file to another file"""
# file4 = open("sample.txt",'r')
# print(file4.read())
#
# file3 = open("sample2.txt",'r')
# print(file3.read())
#
# with open("sample.txt", 'r') as src:
#     with open("sample2.txt", 'a') as dest:
#         contents = src.read()
#         dest.write(contents)
#
# file5 = open("sample2.txt",'r')
# print(file5.read())

"""Write a Python program to read the content of a file and count the 
total number of words in that file."""
# file2 = open("sample.txt",'r')
# print(len(file2.read()))

"""Write a Python program that prompts the user to input a string and converts
it to an integer. Use try-except blocks to handle any exceptions that
might occur"""
# a=input("Enter the string which is to be converted to int:")
# try:
#     b=int(a)
#     print(b,"the string converted to integer")
# except ValueError:
#     print("This string cannot be converted to integer")

"""Write a Python program that prompts the user to input a list of integers
 and raises an exception if any of the integers in the list are negative."""
# a=input("Enter a list of numbers with space:")
# try:
#     b=list(map(int,a.split()))
#     for i in b:
#         if i < 0:
#             raise ValueError("Negative integer found")
#     print("the list of integers:",b)
# except Exception as e:
#     print("Error:",e)

"""Write a Python program that prompts the user to input a list 
of integers and computes the average of those integers. 
Use try-except blocks to handle any exceptions that might occur.
use the finally clause to print a message indicating that the program 
has finished running"""
# a= input("Enter a list of numbers:")
# try:
#     b=list(map(int, a.split(',')))
#     Avg=sum(b) / len(b)
#     print(f"The average of the list of number is:{Avg}")
# except ValueError as e:
#     print("Error:", e)
# except Exception as e:
#     print("Error:",e)
# finally:
#     print("the program has finished running")

"""Write a Python program that prompts the user to input a filename 
and writes a string to that file. Use try-except blocks to 
handle any exceptions that might occur and print a welcome message 
if there is no exception occurred."""
# a =  input("Enter the filename to write:")
# b = input("Enter the sentence to write in the file:")
# try:
#     with open(a,'w') as file:
#         file.write(b)
#     print("The file written successfully.")
# except FileNotFoundError:
#     print("Error: The file could not be found.")
# except IOError:
#     print("Error: An input/output error occurred while writing to the file.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("The program has finished running.")




