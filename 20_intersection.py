
a = [1,2,3,4]
b = [3,4,5]

result = []

for x in a:
    if x in b and x not in result:
        result.append(x)

print(result)