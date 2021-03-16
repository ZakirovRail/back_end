# import json
#
# dict_to_json = {
#     "action": "msg",
#     "to": "account_name",
#     "from": "account_name",
#     "encoding": "ascii",
#     "message": "message"
# }
#
# with open('lesson_2_ex_4.json', 'w') as fn:
#     fn.write(json.dumps(dict_to_json))
# ======================================================================================================================
# import json
#
# dict_to_json = {
#     "action": "msg",
#     "to": "account_name",
#     "from": "account_name",
#     "encoding": "ascii",
#     "message": "message"
# }
#
# with open('lesson_2_ex_4_2.json', 'w') as fn:
#     json.dump(dict_to_json, fn)

# ======================================================================================================================

import json

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}

with open('lesson_2_ex_4_3.json', 'w') as fn:
    json.dump(dict_to_json, fn, sort_keys=True, indent=4)
"""
{
    "action": "msg",
    "encoding": "ascii",
    "from": "account_name",
    "message": "message",
    "to": "account_name"
}
"""
