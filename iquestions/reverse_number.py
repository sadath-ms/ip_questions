"""
Write a program to reverse a number in Python?
"""

def reverse_number():
    rn = int(input('Enter a number: '))
    rev = 0
    
    while(rn >0):
        dig = rn % 10
        rev = rev * 10 + dig
        rn = rn//10
    print("Reverse a number:", rev)    
    
        


if __name__ == '__main__':
    reverse_number()
    