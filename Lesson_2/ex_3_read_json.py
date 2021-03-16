# import json
#
# with open('lesson_2_ex_3.json') as fn:
#     objs = json.load(fn)
#     print(type(objs))  # <class 'dict'>
#
#     str_objs = fn.read()
#     print(type(str_objs))  # <class 'str'>
#     objs_2 = json.loads(str_objs)
#     print(objs_2)

# ======================================================================================================================
# import json
#
# with open('lesson_2_ex_3.json') as fn:
#     objs = json.load(fn)
# for key, value in objs.items():
#     print(key, value)
"""
action msg
to account_name
from account_name
encoding ascii
message message
"""



# ======================================================================================================================

import json

with open('lesson_2_ex_3.json') as fn:

    str_objs = fn.read()
    objs = json.loads(str_objs)
    print(objs)  # {'action': 'msg', 'to': 'account_name', 'from': 'account_name', 'encoding': 'ascii', 'message': 'message'}



