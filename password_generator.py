import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "".join([chr(ord(i)-32) for i in lower])
numbers = "0123456789"
symbols =",./;:?><[]{}\|+=-_!@#$%^&*()~`"

password = lower + upper + numbers + symbols
length = int(input())
print("".join(random.sample(password, length)))