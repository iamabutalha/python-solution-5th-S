arr = [1,2,3,44,44]

seen = []
for n in arr:
    if n in seen:
        print(n)
        break
    seen.append(n)

print(seen)