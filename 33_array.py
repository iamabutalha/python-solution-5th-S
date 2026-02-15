def mergeNestedArray(arr):
    newArr = []
    for ch in arr:
        if isinstance(ch, list):
            mergeNestedArray(ch)
        else:
            newArr.append(ch)
    return newArr
    
print(mergeNestedArray([1,2,[3,4]]))