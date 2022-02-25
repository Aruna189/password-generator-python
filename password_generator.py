import random # Importing random module which selects characters randomly
'''
Defining all possible characters
'''
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "".join([chr(ord(i)-32) for i in lower]) # Using list comprehension and ascii manipulation functions
numbers = "0123456789"
symbols =",./;:?><[]{}\|+=-_!@#$%^&*()~`"

password = lower + upper + numbers + symbols
length = int(input()) # Getting input for the length of the password
print("".join(random.sample(password, length)))
