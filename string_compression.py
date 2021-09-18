"""
String Compression

Given the string in the form of AAABBBCCCDDDD compress it to A3B3C3D4
"""

def string_compression(st):
    r = ""
    length = len(st)
    
    if length == 0:
        return ""
    
    if length == 1:
        return st + "1"
    
    last = st[0]
    cnt = 1
    i = 1
    while i < length:
        if st[i] == st[i-1]:
            cnt +=1
        else:
            r = r + st[i-1] + str(cnt)
            cnt = 1
        i+=1
    
    r = r + st[i-1] + str(cnt)
    return r
    
    


if __name__ == '__main__':
    st = 'AAABBBCCCDDDDA'
    result = string_compression(st)
    print(result)
    