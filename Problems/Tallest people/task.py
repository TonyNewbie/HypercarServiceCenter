def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    list_keys = list(kwargs.keys())
    list_keys.sort()
    for key in list_keys:
        if kwargs[key] == max_height:
            print(key, ':', kwargs[key])
