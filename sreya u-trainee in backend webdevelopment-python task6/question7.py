# 7.Write a Python program to Delete a list of keys from a dictionary


dict = {'val1': 1, 'val2': 2, 'val3': 3, 'val4': 4, 'val5': 5}

rem_list = ['val3', 'val4']

for key in rem_list:
   if key in dict:
       dict.pop(key)

print("Dictionary after removal of keys : ", dict)