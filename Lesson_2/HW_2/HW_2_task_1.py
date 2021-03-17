import csv
import chardet
list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
list_files_1 = ['info_1.txt',]


def get_data(list_files):
    data_list = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    data_to_export = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in list_files:
        with open(file, 'r', encoding='windows-1251') as f:
            for line in f:
                data_list.append(line.split(': '))  # [['Имя узла','Comp1\n'], ['Название ОС', 'Microsoft Windows 7 Профессиональная \n']]
    # for regular expression \s*\S+
    for x in data_list:
        if x[0] == 'Изготовитель системы':
            os_prod_list.append(x[1].strip(' \n'))
        elif x[0] == 'Название ОС':
            os_name_list.append(x[1].strip(' \n'))
        elif x[0] == 'Код продукта':
            os_code_list.append(x[1].strip(' \n'))
        elif x[0] == 'Тип системы':
            os_type_list.append(x[1].strip(' \n'))
    data_to_export.append(main_data)
    data_to_export.append(os_prod_list)
    data_to_export.append(os_name_list)
    data_to_export.append(os_code_list)
    data_to_export.append(os_type_list)
    # print(data_to_export)
    return data_to_export


def write_to_csv(data):
    with open('task_1.csv', 'w') as file:
        fn_write = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            fn_write.writerow(row)


data = get_data(list_files)
write_to_csv(data)
