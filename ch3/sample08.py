my_book=2002,'파이썬',200
my_book2=2002,'파이썬',200

print(type(my_book))
print(my_book)

print(type(my_book2))
print(my_book2)

year,title=my_book #개수만큼 변수선언
print(year)
print(title)

print('-------------------------------')
print(my_book[0])
print(my_book[1])
print(my_book[2])
#print(my_book[3])은 에러
print('-------------------------------')
print(my_book[-3])
print(my_book[-2])
print(my_book[-1])
#print(my_book[-4])은 에러

print(len(my_book))

print(my_book[len(my_book)-1])