nums = [1,2,3,4,4,4,4,5]

largest = second = float("-inf")

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)