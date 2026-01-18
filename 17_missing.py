

def checkMissing(arr):
    newArr = []
    for num in arr:
        if type(num) != None:
            newArr.append(num)
    return newArr

print(checkMissing([1,2,3,None]))