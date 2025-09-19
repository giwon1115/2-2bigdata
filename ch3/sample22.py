#딕셔너리
#키:값

data={'bgnde':'2025.03.01','sj':'삼일절','endde':'2025.03.01'}

print(data)
print(type(data))

print(data['sj'])
data['desc']='삼일절은 휴강입니다'#새로운 키 추가

print(data)

data['endde']='2025.04.01'#키는 유일 추가해도 안 바뀜
print(data)

data_key_list=data.keys()
print(data_key_list)
print(type(data_key_list))

for key in data.keys():
    print(key)
for value in data.values():
    print(value)

print('-----------------')

for item in data.items():
    print(item)
    print(item[0],item[1])

