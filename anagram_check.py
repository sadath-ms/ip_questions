# python program to check a string is anagram or not using set() function
def anagram_check_s1(str1, str2):
    
    if len(str1) != len(str2):
        # strings are not in same length
        return False
    
     # Implementation of set function
    return True if set(str1.lower()) == set(str1.lower()) else False

def anagram_check_s2(str1, str2):
    
    if len(str1) != len(str2):
        # strings are not in same length
        return False
    
    counter = dict()
    
    for letter in str1:
       if letter in counter:
           counter[letter] +=1
       else:
           counter[letter] = 1
    
    for letter in str2:
        if letter in counter:
           counter[letter] -=1
        else:
           counter[letter] = 1
    
    for k in counter:
        if counter[k] != 0:
            return False
    
    return True
    
if __name__ == '__main__':
    str1 = 'listen'
    str2 = 'silend'
    result = anagram_check_s2(str1,str2)
    print(result)
    