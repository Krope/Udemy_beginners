def say_hi(): # Простейшая функция
    print('Hi!')

say_hi() #вызов функции

#функция с одним  параметром
def sayHi(name):
    print('Yi {}!'.format(name))

sayHi('Jason')
sayHi('everybody')

#функции с несколькими параметрами
def say_hi(first, last):
    print('Hi {} {}!'.format(first, last))

say_hi('Jane', 'Doe')


#функции с присвоением аргументов
def say_hi(first, last):
    print('Hi {} {}!'.format(first, last))

say_hi(first = 'Jane', last = 'Doe')
say_hi(first = 'Doe', last = 'Jane')

def say_hi(first, last = 'Doe'):
    print('Hi {} {}!'.format(first, last))

say_hi('Jane')
say_hi('Jane', 'Carolina')
