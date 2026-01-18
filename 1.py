# Write a program that take a list of nums from user and calculate the even sum


# Method 1
# using function
def sumEven(arr):
    sum = 0

    for i in arr:
        # if even do add it to sum
        if i % 2 == 0:
            sum += i
        
    
    return sum
# take arr from user or you can provide a static list like
# print(sumEven([1,2,3,4,5,6]))
arr = []
for  i in range(5):
    num = int(input(f"Enter num at index {i}: "))
    arr.append(num)
print("Your list aka array is ", arr)
print(sumEven(arr))

print("------------------------")

# Method 2
# without function
# we take list of 5 nums
lst = []

# get values from user
for i in range(5):
    # parse the input to int -> "explicit typecasting"
    num = int(input(f"Enter value at index {i} "))
    # put the value in the list we created
    lst.append(num)

# print the array/list -> to se the values init

print("list values are ", lst)

even_count = 0

for num in lst:
    if num % 2 == 0:
        even_count += num
    

print(even_count)



