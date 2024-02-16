# 5.	Write a Python program to multiply all the items in a dictionary.

dict_1={"val1":12,"val2":20,"val3":3}

product = 1
for value in dict_1.values():
    product *= value
    
print("product of all values in dictionary is:",product)