age_inp = input('How old are you: ')
age = int(age_inp)
if age >= 35:
    print('You are old enough to be a Representative, Senator or the President.')
elif age >= 30:
    print('You are old enough to be a Senator.')
elif age >= 25:
    print('You are old enough to be a Representative.')
else:
    print('You are not old enough to be a Representative, Senator or the President.')
print('Have a nice day')
