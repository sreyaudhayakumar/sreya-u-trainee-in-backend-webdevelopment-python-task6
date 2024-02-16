# 3.Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are the square of the keys

dict_1 = {}

user_input = int(input("Enter the range for which you need square numbers: "))

for i in range(1, user_input + 1):
    dict_1[i] = i ** 2

print("Square of numbers from 1 to", user_input, "is:", dict_1)
