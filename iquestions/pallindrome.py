"""
Write a Python Program to Check if a Number is a Palindrome or not?
"""

def palindrome_number():
    n = int(input("enter a number"))
    temp = n
    rev = 0
    
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n//10
    result = "is a pallindrome number" if temp == rev else 'not pallindrome' 
    print(result)
    
def pallindrome_string():
    n = list(input('Enter a sting:-'))
    result = "is a pallindrome stirng" if n == list(reversed(n)) else 'not pallindrome' 
    print(result)

        
    

if __name__ == '__main__':
    pallindrome_string()
    