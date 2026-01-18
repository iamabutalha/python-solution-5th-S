
def isPalindrome(str):

    # reverse_str = ""
    # for i in range(len(str), -1, -1):
    #     print(str[i])
    #     # reverse_str += str[i]

    return str[::-1] == str

print(isPalindrome("civic"))
        