def dict_values_to_str(dictionary):
    for index in dictionary:
        value = dictionary[index]

        if isinstance(value, dict):
            dictionary[index] = dict_values_to_str(value)

        elif isinstance(value, (list, tuple,)):
            dictionary[index] = [str(v) for v in value]

        else:
            dictionary[index] = str(value)

    return dictionary