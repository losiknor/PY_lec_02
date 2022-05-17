# СЛОВАРИ
from turtle import down, left, right


dictionary = {} # задать пустой словарь
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
for k in dictionary.keys():
    print(k)    # up
                # left
                # down
                # right
for k in dictionary.values():
    print(k)    # ↑
                # ←
                # ↓
                # →
for v in dictionary:
    print(v)    # up
                # left
                # down
                # right
for v in dictionary:
    print(dictionary[v])    # ↑
                            # ←
                            # ↓
                            # →
print('')
print(dictionary['up'])
dictionary['up'] = 'ups'
print(dictionary['up'])