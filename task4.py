# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка -
# были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
order= dict(zip(keys, values))
print(order)

