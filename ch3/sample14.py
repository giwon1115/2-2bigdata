from ch3.sample11 import your_book
from ch3.sample13 import new_book

your_book=[2002,'파이썬',200,'1교시']
new_book=your_book

print(your_book)
print(new_book)

your_book[0]=2025
print('------------------')
print(your_book)
print(new_book)

new_book=your_book[:]
print('--------------')
print(your_book)
print(new_book)
your_book[0]=2026
print('-------------------')
print(your_book)
print(new_book)