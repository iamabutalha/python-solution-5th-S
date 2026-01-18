def check_list_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            is_sorted = False
            return "Not sorted"
        
    print("List is sorted")

print(check_list_sorted([1,2,3,10,6])
)