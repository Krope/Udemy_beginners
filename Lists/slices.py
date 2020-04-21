list[index1:index2]
list[:index2]
list[index1:]

animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

# Выбор нескольких значений из списка
some_animals = animals[1:4]
print('Some animals:    {}'.format(some_animals))

# вывод первых двух значений списка
first_two = animals[0:2]
print('First two animals: {}'.format(first_two))

# второй способ вывода первых двух значений из списка
first_two_again = animals[:2]
print('First two animals {}'.format(first_two_again))

# Вывод последних двух значений из списка
last_two = animals[4:6]
print('Last two animals {}'.format(last_two))

# Второй способ вывода последних двух значений из списка
last_two_again = animals[-2:]
print('Last two animals {}'.format(last_two_again))
