# create a function count_vowels that take a string and return the number of vowels in it


# Method 1:
def count_vowels(str):
    count = 0

    for char in str:
        if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "u" or char == "U":
            count += 1
            
        
    return count
    

print(count_vowels("Remember the name leo messi")) # -> 9
print(count_vowels("that fuvking nobody is jhonwick")) # -> 5
print(count_vowels("I am the ghost of the uchicha. Madra Uchicha"))

print("-----------------------------------")


# Second Method

def count_vowels2(str):
    vowles = 'aeiouAEIOU'
    count = 0
    for char in str:
        if char in vowles:
            count += 1
        
    return count


print(count_vowels2("Hai laila na ky rab sy faryad")) 
print(count_vowels("My name is shrader.. ASAC shrader!"))
print(count_vowels2("My name is optimus prime"))




    

