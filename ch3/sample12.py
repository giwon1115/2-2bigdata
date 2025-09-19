from ch3.sample11 import your_book

my_book=[2002,'파이썬',200]
print(type(your_book))
print(my_book)

#기존 데이터 변경
your_book[0]=2025
print(your_book)

#추가
your_book.append('파이썬 프로그래밍')
print(your_book)
your_book.insert(1,'프로그래밍과목')
print(your_book)

if'파이썬2'in your_book:
    your_book.remove('파이썬')#없는값을 삭제하면 에러
print(your_book)