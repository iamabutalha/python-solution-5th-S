data = {"a": 1, "b": 1}

reversed_dict = {}

for key, value in data.items():
    reversed_dict[value] = key


print(reversed_dict)