a = 'строка'

try:
    bytes('строка')
except UnicodeError:
    print('Error message')
