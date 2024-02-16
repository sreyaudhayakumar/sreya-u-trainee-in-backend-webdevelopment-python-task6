# 8.	Create a function that takes a string 
# and returns a dictionary where keys are letters, and 
# values are the number of times each letter appears in the string 

def count_letters(string):
    letter_count = {}
    for char in string:
        if char.isalpha():  
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

input_string = str(input("enter the string:"))
result = count_letters(input_string)
print(result)
