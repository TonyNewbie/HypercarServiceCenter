def startswith_capital_counter(name_list):
    counter = 0
    for name in name_list:
        if isinstance(name, str):
            if name[0].isupper():
                counter += 1
    return counter
