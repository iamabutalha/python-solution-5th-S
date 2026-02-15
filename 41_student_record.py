students = ['talha', 'kashif', 'wali']
list_total = []
total = 0
marks = [
    [10, 20, 30, 40],
    [90, 80, 60, 50],
    [67, 68, 69, 80 ]
]

for mark in marks:
    for num in mark:
        total += num
    print(total)
    list_total.append(total)


for i in range(0, 3):
    print(f"Student name is {students[i]} having {list_total[i]}" )