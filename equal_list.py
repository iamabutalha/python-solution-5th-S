a = [1,2,3]
b = [3,2,1]

equal = True
for item in a:
    if a.count(item) != b.count(item):
        equal = False
        break
    print(equal)