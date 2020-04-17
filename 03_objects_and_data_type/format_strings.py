print('Эта строка была {}'.format('добавлена'))
print('у меня есть {} {} {}'.format('вкусное', 'красное', 'яблоко'))
print('у меня есть {2} {1} {0}'.format('вкусное', 'красное', 'яблоко'))
print('у меня есть {v} {k} {y}'.format(v='вкусное', k='красное', y='яблоко'))
print('у меня есть {y} {y} {y}'.format(v='вкусное', k='красное', y='яблоко'))

# value:width.precisionf
result = 100 / 777
print(result)
print('Резульат:{r:1.3f}'.format(r=result))

# position:width
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# Fruit    | Quantity
# Apples   |       3.0
# Oranges  |        10

# aline < ^ >

print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))
# Left     |  Center  |    Right
# 11       |    22    |       33
# 11====== | ---22--- | ......33

name = 'Alehandro'
print(f'Имя: {name}')
print(f'Имя: {name!r}')
# Имя: 'Alehandro'

# {value:{width}.{precision}}
print(f'Результат:{result:{7}.{3}}')
print(f'Результат:{result:8.3f}')
