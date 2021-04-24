### Given a string, write a python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “malayalam” is a palindrome, but “music” is not a palindrome

def palindrome(str):
    # rev_string=''
    # for i in range((len(str)-1), -1, -1):
    #     rev_string += str[i]
    # if str == rev_string:
    #     print(f'{str} is palindrome')
    # else:
    #     print(f'{str} is not palindrome')
    str = str.replace(" ", "")
    return str == str[::-1]

print(palindrome("malayalam"))

print(palindrome("music"))

print(palindrome("nurses run"))
