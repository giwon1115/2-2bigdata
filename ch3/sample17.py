import copy

from ch3.sample11 import your_book
from ch3.sample13 import new_book
tuple_value=('1','2','3')
list_value=['4','5','6']

print(tuple_value)
print(list_value)

tuple_to_list=tuple(list_value)
print(tuple_to_list)

list_to_tuple=list(tuple_value)
print(list_to_tuple)
