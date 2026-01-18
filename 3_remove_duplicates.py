# Given a list of integers write a program to remove duplicate element form the list without using set()

# Method 1 (with function)
# Note In python array and list is the same thing


def remove_duplicate(arr):
    new_arr = []
    for num in arr:
        if not num in new_arr:
            new_arr.append(num)
    
    return new_arr

print(remove_duplicate([1,2,2,2,3]))

print("-------------------")

# Method 2 (non function)
lst = [1,2,2,2,3,4,4,4]
new_lst = []
for num in lst:
    if num not in new_lst:
        new_lst.append(num)

print(new_lst)

