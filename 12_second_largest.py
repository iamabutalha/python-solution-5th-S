# Check Second largest in a list

nums = [1,22,134,44,33]
largest = -1
second = -1

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)