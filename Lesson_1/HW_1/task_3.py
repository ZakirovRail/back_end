word_dict = ['attribute', 'класс', 'функция', 'type']
charset = 'utf-8'
wrong_words = []
encoded_words = []

for word in word_dict:
    try:
        encoded_words.append(word.encode('ascii'))
        print(f'The following word we can encode to ascii "{word}"')
    except:
        wrong_words.append(word)

for word in wrong_words:
    print(f'The following word we can not encode to ascii - "{word}"')
