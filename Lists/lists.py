# Create Lists
list_name = [item_1,item_2,item_3]
list_name = []
list_name[index]

# Example
animals = ['man', 'bear', 'pig']
print(animals[0])
print(animals[1])
print(animals[2])

#Отрицательные индексы списков (изменяют порядок вызова значения в обратную сторону)
animals = ['man', 'bear', 'pig']
print(animals[-1])
print(animals[-2])
print(animals[-3])

# Добавление нового значения в список
animals = ['man', 'bear', 'pig']
animals.append('cow')
print(animals[-1])

# Присоединение списка к списку с помощью .extend()
animals = ['man', 'bear', 'pig']
animals.extend(['cow', 'duck'])
print(animals)

more_animals = ['horse', 'dog']
animals.extend(more_animals)
print(animals)

#Добавление значения в список с присвоением индекса
animals = ['man', 'bear', 'pig']
animals.insert(0, 'horse')
print(animals)

animals.insert(2, 'duck')
print(animals)
