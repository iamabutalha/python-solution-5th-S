# with for loop print factorail of a num

num = int(input("Enter a num: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)