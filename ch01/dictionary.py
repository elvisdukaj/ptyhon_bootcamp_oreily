dic = {
       'key': 'value',
       'key2': 'another value',
       2: 3,
       3: 'value3'
       }

print(f'{type(dic)}: {dic}')
print(f'key is {dic["key"]}')

dic['something_new'] = [1, 2, 3]
print(f'{type(dic)}: {dic}')

dic['something_new'] = 1
print(f'{type(dic)}: {dic}')

del dic['something_new']
print(f'{type(dic)}: {dic}')

dic[1] = {'another key': 1}
print(f'{type(dic)}: {dic}')

print(dic.get(4))
print(dic.get(4, 'not exists'))

dic.setdefault('t', 0)
print(f'{type(dic)}: {dic}')

dic.setdefault('t', 1)
print(f'{type(dic)}: {dic}')
