"""
UNIQUE CHARCTER IN A STRING

Given a string determines, if it is compresied of all unique characters,for example 
the string 'abcde' has all unique characters it retrun True else False
"""

def unique_char(st):
    return len(set(st)) == len(st)

def unique_char_v2(st):
    
    chars = set()
    
    for u in st:
        if u in chars:
            return False
        else:
            chars.add(u)
    return True

if __name__ == '__main__':
    st = "sadath"
    result = unique_char_v2(st)
    print(result)
    