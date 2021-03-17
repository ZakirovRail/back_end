# import csv
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['kp1', 'Cisco', '2960', 'Moscow, str'],
#         ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
#         ['kp3', 'Cisco', '2960', 'Kazan, str'],
#         ['kp4', 'Cisco', '2960', 'Tomsk, str']]
#
#
# with open('lesson_2_ex_2.csv', 'w') as fn:
#     fn_write = csv.writer(fn)
#     for row in data:
#         fn_write.writerow(row)

# ======================================================================================================================
# import csv
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['kp1', 'Cisco', '2960', 'Moscow, str'],
#         ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
#         ['kp3', 'Cisco', '2960', 'Kazan, str'],
#         ['kp4', 'Cisco', '2960', 'Tomsk, str']]
#
#
# with open('lesson_2_ex_2_2.csv', 'w') as fn:
#     fn_write = csv.writer(fn, quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         fn_write.writerow(row)

# ======================================================================================================================
# import csv
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['kp1', 'Cisco', '2960', 'Moscow, str'],
#         ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
#         ['kp3', 'Cisco', '2960', 'Kazan, str'],
#         ['kp4', 'Cisco', '2960', 'Tomsk, str']]
#
#
# with open('lesson_2_ex_2_3.csv', 'w') as fn:
#     fn_write = csv.writer(fn, quoting=csv.QUOTE_NONNUMERIC)
#     fn_write.writerows(data)

# ======================================================================================================================

import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]


with open('lesson_2_ex_2_4.csv', 'w') as fn:
    fn_write = csv.writer(fn, delimiter='*')
    fn_write.writerows(data)
