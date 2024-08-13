import numpy as np
from Functions_of_code import sort_list_ascending

lst = []
print("Enter 5 numbers to sort:")
for n in range(1,6):
    ele = int(input())
    lst.append(ele)
print(lst)
sort_list_ascending(lst)
print(lst)
        
print(np.array_split(lst,2))