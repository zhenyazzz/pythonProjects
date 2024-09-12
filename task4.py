my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
top_3 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(top_3)


