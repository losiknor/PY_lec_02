# МНОЖЕСТВА

colors = {'red', 'green', 'blue'}
print(type(colors))
print(colors)
colors.add('red') # не добавится т.к. точно такой же уже есть
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# colors.remove('red') # если удалять не существующий, то получим ошибку
colors.discard('red') # удаление без ошибки, если и не существует
print(colors)
colors.clear() # очищение множества
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # копирование
u = a.union(b) # объединение
i = a.intersection(b) # пересечение
dl = a.difference(b)
dr = b.difference(a)
s = frozenset(a) # замороженное множество