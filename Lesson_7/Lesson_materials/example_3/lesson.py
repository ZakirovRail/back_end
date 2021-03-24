# class Cars(object):
#     model: str
#     color: str
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#
# my_car = Cars('ford', 'blue')
# print(my_car.__dict__)  # {'model': 'ford', 'color': 'blue'}
# my_car.weight = 1200
# print(my_car.__dict__)  # {'model': 'ford', 'color': 'blue', 'weight': 1200}

# ==========================================================================
class Cars(object):
    __slots__ = ('model', 'color')  # we strictly define which attributes should be in the class Cars

    def __init__(self, model, color):
        self.model = model
        self.color = color


my_car = Cars('ford', 'blue')
print(my_car)  # <__main__.Cars object at 0x7f9205286640>
my_car.weight = 1200
print(my_car)
"""
AttributeError: 'Cars' object has no attribute 'weight'
"""




