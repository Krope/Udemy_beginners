how_far = input("How far you want to travel: ")
try:
    distance = int(how_far)
except:
    print('Please, input correct number')


if distance <= 3:
    print('Вы можете пройти этот путь пешком.')
elif distance >= 3 and distance <= 300:
    print('You can drive this path.')
elif distance >= 300:
    print('You can fly this path.')
else:
    print('Have a safe journey')
