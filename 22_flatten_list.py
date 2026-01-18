
nested_list = [1, [2,3], [4, [5]]]

def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
    return flat
    
print(flatten(nested_list))
