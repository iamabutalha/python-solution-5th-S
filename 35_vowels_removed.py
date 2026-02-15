def vowels_removed(str) -> str:
    vowels = "aeiouAEIOU"
    final_str = ""

    for char in str:
        if char not in vowels:
            final_str += char
    
    return final_str

print(vowels_removed("My name is walter hartwell white"))