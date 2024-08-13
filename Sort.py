import numpy as np
lst = []
print("Enter 5 numbers to sort:")
for n in range(1,6):
    ele = int(input())
    lst.append(ele)
lst = np.sort(lst)
print(lst)
