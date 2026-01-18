
str = "abbbcdef"
freq = {}

for ch in str:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

