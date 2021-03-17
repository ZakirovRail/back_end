import csv

data_to_export = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'], ['LENOVO', 'ACER', 'DELL'], ['Microsoft Windows 7 Профессиональная', 'Microsoft Windows 10 Professional', 'Microsoft Windows 8.1 Professional'], ['00971-OEM-1982661-00231', '00971-OEM-1982661-00231', '00971-OEM-1982661-00231'], ['x64-based PC', 'x64-based PC', 'x86-based PC']]


def write_to_csv(list):
    with open('task_1.csv', 'w') as file:
        fn_write = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
        for row in data_to_export:
            fn_write.writerow(row)

write_to_csv(data_to_export)
# with open('lesson_csv.csv', 'w') as fn:
#     fn_write = csv.writer(fn)
#     for row in data:
#         fn_write.writerow(row)