days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
    print(day)

# Перевод кортежа в список
weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
print('weekend_tuple is {}.'.format(type(weekend_tuple)))
print('weekend_list is {}.'.format(type(weekend_list)))

# Перевод списка в кортеж
animals_list = ['man', 'bear', 'pig']
animals_tuple = tuple(animals_list)
print('animals_list is {}.'.format(type(animals_list)))
print('animals_tuple is {}.'.format(type(animals_tuple)))

# Присвоение ключей кортежу
weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)

contact_info = ['555-0123', 'jason@example.com']
(phone, email) = contact_info
print(phone)
print(email)

# Использование кортежей в функциях
def high_and_low(numbers):
    """Determine the hidhest and lowest number"""

    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is: {}'.format(lowest))

# Цикл с двумя значениями в кортежах
contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]

for (name, phone) in contacts:
    print("{}'s pnone is {}.".format(name, phone))
