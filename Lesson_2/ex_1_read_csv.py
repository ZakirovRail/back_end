# import csv
#
# with open('kp_data.txt') as fn:
#     fn_reader = csv.reader(fn)
#     print(list(fn_reader))  # [['hostname', 'vendor', 'model', 'location'], ['kp1', 'Cisco', '2960', 'Moscow'],
#     # ['kp2', 'Cisco', '2960', 'Novosibirsk'], ['kp3', 'Cisco', '2960', 'Kazan'], ['kp4', 'Cisco', '2960', 'Tomsk']]
#     for row in fn_reader:
#         print(row)
#     print(fn_reader)  # <_csv.reader object at 0x7fcb3b3179e0>
#     print(format(fn_reader))  # <_csv.reader object at 0x7fcb3b3179e0>
#     print(type(fn_reader))  # <class '_csv.reader'>
#     print(list(fn_reader))  # []

# # ======================================================================================================================
# import csv
#
# with open('kp_data.txt') as fn:
#     fn_reader = csv.reader(fn)
#     # to get headers in a list
#     fn_headers = next(fn_reader)
#     # to print only headers
#     print(fn_headers)  # ['hostname', 'vendor', 'model', 'location']
#     for row in fn_reader:
#         print(row)
"""
['kp1', 'Cisco', '2960', 'Moscow']
['kp2', 'Cisco', '2960', 'Novosibirsk']
['kp3', 'Cisco', '2960', 'Kazan']
['kp4', 'Cisco', '2960', 'Tomsk']
"""
# ======================================================================================================================
import csv

with open('kp_data.txt') as fn:
    fn_reader = csv.DictReader(fn)
    print(fn_reader)  # <csv.DictReader object at 0x7f977602efd0>
    for row in fn_reader:
        print(row)
"""
{'hostname': 'kp1', 'vendor': 'Cisco', 'model': '2960', 'location': 'Moscow'}
{'hostname': 'kp2', 'vendor': 'Cisco', 'model': '2960', 'location': 'Novosibirsk'}
{'hostname': 'kp3', 'vendor': 'Cisco', 'model': '2960', 'location': 'Kazan'}
{'hostname': 'kp4', 'vendor': 'Cisco', 'model': '2960', 'location': 'Tomsk'}
"""

# ======================================================================================================================



