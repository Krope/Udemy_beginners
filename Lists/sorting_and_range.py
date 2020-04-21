animals = ['man', 'bear', 'pig']
# сортировка значений по алфавиту
sorted_animals = sorted(animals)
#выводи начальные значения
print('Animals list:        {}'.format(animals))
#выводит отсортированные значения
print('Sorted animals list: {}'.format(sorted_animals))
# второй способ сортировки значений по алфавиту
animals.sort()
print('Animals after sort method: {}'.format(animals))

# Конкатенация несколький списков
animals = ['man', 'bear', 'pig']
more_animals = ['cow', 'duck', 'horse']
all_animals = animals + more_animals
print(all_animals)

# длина списка
animals = ['man', 'bear', 'pig']
print(len(animals))
animals.append('cow')
print(len(animals))

# ===ДИАПАЗОНЫ===

#Выводит все значения до 3
for number in range(3):
    print(number)

# Выводит все нечетные значения до 10
for number in range(1, 10, 2): # в range(начало, конец, шаг)
    print(number)

animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']
for number in range(0, len(animals), 2):
    print(animals[number])

list1 = [3, 4, 5, 6, 5]
print(len(list1))
