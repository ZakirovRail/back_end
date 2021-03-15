import chardet

text_data = ['сетевое программирование', 'сокет', 'декоратор']

print('start writing to the file')
with open('test_file.txt', 'w') as f:
    for word in text_data:
        print(word)
        f.write(str(word) + '\n')

print('='*50)
print('start reading from the file')
f = open('test_file.txt', 'rb').read()
charset = chardet.detect(f)['encoding']
print(f'The encoding type is {charset}')
print(f.decode('utf-8'))
