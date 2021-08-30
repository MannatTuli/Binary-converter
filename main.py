import os 
import sys

code = input('Enter the string to convert to binary: ')

array = bytearray(code, "utf8")

listBinary = []

for byte in array:
    binary = bin(byte)
    listBinary.append(binary)
    print(binary)

print('List:')
print(listBinary)