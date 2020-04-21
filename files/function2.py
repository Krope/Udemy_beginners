def say_hi(first, last = 'Doe'):
    """Say hello."""
    print('Hi {} {}!'.format(first, last))

help(say_hi)

# определение четного или нечетного числа
def odd_or_even(number):
    """"Determine if a number is odd or even."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

number = input('Please input number:')
odd_or_even_string = odd_or_even(int(number))
print(odd_or_even_string)

# определение четного или нечетного числа с выводом True или False
def is_odd(number):
    """Determine if a number is odd."""
    if number % 2 == 0:
        return False
    else:
        return True

number = input('Please input number:')
print(is_odd(int(number)))

# Функции, которые вызывают другие функции
def get_name():
    name = input('What is your name? ')
    return name

def say_name(name):
    print('Your name is {}.'.format(name))

def get_and_say_name():
    """Get and display name"""
    name = get_name()
    say_name(name)

get_and_say_name()
