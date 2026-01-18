
def word_count(str):
    count = {}
    words = str.split(" ")
    for word in words:
        count[word] = len(word)
    
    print(count)

print(word_count("Hello world"))