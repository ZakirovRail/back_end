list_var = ['администрирование', 'protocol', 'standard']


for var in list_var:
    print(f'The word "{var}" is encoded to utf-8 -> {var.encode("utf-8")}')
    print(f'The word "{var}" is decoded in utf-8 charset -> {(var.encode("utf-8")).decode("utf-8")}')