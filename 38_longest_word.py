s = 'DSA IS POWERFUL IN Te whole coding process'

def longestWord(arr):
    words = arr.split(" ")
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
        
    return longest

print(longestWord(s))