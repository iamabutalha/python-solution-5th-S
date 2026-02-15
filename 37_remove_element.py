arr = [1,2,3,4,5]
key = 3

def removeElement(arr, key):
    result = []
    for n in arr:
        if n != key:
            result.append(n)
    return result

print(removeElement(arr, key))