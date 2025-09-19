import copy

from ch3.sample11 import your_book
from ch3.sample13 import new_book

list_value_1=['1','2','3']
list_value_2=['4','5','6']

list_value_1.extend((list_value_2))

print(list_value_1)
print(list_value_2)
'''
print(id(list_value_1))
print(id(list_value_2))

list_value_1=list_value_1+list_value_2
print(list_value_1)
print(list_value_2)

print(id(list_value_1))#주소 달라짐
print(id(list_value_2))
'''
