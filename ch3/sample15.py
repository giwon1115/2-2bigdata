import copy

from ch3.sample11 import your_book
from ch3.sample13 import new_book

list_value=['1','2','3','4','5','6','7','8']
new_list_value=list_value[:]

print(list_value)
print(new_list_value)

list_value[0]=11
print('--------------------')
print(list_value)
print(new_list_value)
print('-------------------')
list_value=[['1','2'],['3','4'],['5','6'],['7','8']]
print(len(list_value))
new_list_value=copy.deepcopy(list_value)#완전히 새롭게 메모리에 만들어짐


print(list_value)
print(new_list_value)

list_value[0][0]='11'
print('-------------------------')
print(list_value)
print(new_list_value)

del new_list_value
print(new_list_value)