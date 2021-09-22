"""
Write a program to find the sum of the digits of a number in Python?
"""

def sum_digits():
    d = int(input('Enter the number: '))
    total = 0
    
    while d > 0:
        dig = d % 10
        total = total + dig
        d = d // 10
    
    print("total:-", total)
    

if __name__ == '__main__':
    sum_digits()
    