#Экранирование специальных символов
sentence = 'She said, "That is a great tasting apple"' # при помощи комбинирования одинарных и двойных кавычек
sentence = "She said, \"That's a great tasting apple\"" #при помощи символоа \
sentence = 'She said, "That\'s a great tasting apple"'

# Перевод строки в верхний/нижний регистр
fruit = 'apple'
print(fruit.lower()) # Перевод строки в нижний регистр
print(fruit.upper()) # Перевод строки в верхний  регистр

# конкатенация строк


animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'

print('Here is an animal, a vegetable, and a mineral')
print(animal)
print(vegetable)
print(mineral)





















animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'
print('Here is an animal, a vegetable, and a mineral.', + animal, + vegetable)
