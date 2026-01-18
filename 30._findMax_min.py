arr = [3,1,7,8,9]

max_val = arr[0]
min_val = arr[0]

for n in arr:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print(max_val, min_val)