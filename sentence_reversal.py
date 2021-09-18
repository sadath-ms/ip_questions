"""
Sentence reversal:
    Given a string of words, reverse all words . For example:
    
    This is the best 
    best is the This
"""

def reverse_sentence_v1(st):
    return " ".join(reversed(st.split()))

def reverse_sentence_v2(st):
    return " ".join(st.split()[::-1])

def reverse_sentence_v3(st):
    
    words = []
    length = len(st)
    
    i = 0
    
    while i < length:
        
        if st[i] != ' ':
            word_start = i
            while i < length and st[i] != ' ':
                i+=1
            
            words.append(st[word_start:i])
        i+=1
    return ' '.join(reversed(words)) 

if __name__ == '__main__':
    st = "This is the best"
    result = reverse_sentence_v3(st)
    print(result)
    