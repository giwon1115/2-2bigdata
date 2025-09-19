from ch3.sample11 import your_book

my_book=(2002,'파이썬',200)
your_book=[2002,'파이썬',200,'1교시']
other_book=your_book
print(your_book)
print(my_book)
print(other_book)

print(id(your_book))
print(id(my_book))
print(id(other_book))

new_book=your_book[1:2+1]
print(new_book)

new_book2=my_book[1:3]
print(new_book2)

print('------------------')
other_book=[your_book[0],your_book[1],your_book[2],your_book[3]]
#other_book=your_book[:]
print('my_book: ',my_book)
print('your_book:',your_book)
print('other_book:',other_book)

print(id(your_book))
print(id(my_book))
print(id(other_book))