contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

for contact in contacts:
    print('Time number for {0} is {1}.'.format(contact, contacts[contact]))

# Циклы с двумя значениями
for key_variable, value_variable in dictionary_name.items():
    #Code block

contacts = {
    'Jason': '555-0123',
    'Carl': '555-0987'
}

for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))

# Вложенные словари
contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Carl': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    }
}

for contact in contacts:
    print("{}'s contact info:".format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])
