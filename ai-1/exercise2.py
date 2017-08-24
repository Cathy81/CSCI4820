list1=['test', 'LongTest', 'BLAHblah']

list2 = [x.lower() for x in list1 if len(x)>5]

print(list2)