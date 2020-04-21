# Поиск значения в списке
animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
print(bear_index)
# Исключения, если значения нет в списке, возникнет ошибка
animals = ['man', 'bear', 'pig']
cat_index = animals_index('cat')
print(cat_index)


animals = ['man', 'bear', 'pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cats found'

print(cat_index) 
