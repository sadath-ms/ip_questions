"""
1 - Write a Python Program to Count the Number of Digits in a Number?
"""

def digit_count():
    d = int(input("Enter digit "))
    dig = 0
    
    while d > 0:
        dig = dig+1
        d = d//10
        
    print("total digits",dig)
    

"""
2 -  Write a Python Program to Print Table of a Given Number?
"""

def table_m():
    n = int(input("enter the number to print table: "))
    for i in range(1, 11):
        print(str(n) + '*' + str(i) + "="+ str(n*i))


"""
3 - Write a Python Program to Check if a Number is a Prime Number?
"""

def check_prime_no():
    n = int(input('Enter a prime number'))
    k = 0
    
    for i in range(2, n//2+1):
        if (n % i == 0):
            k = k+1
        
    if (k <=0):
        print("Number is prime")
    else:
        print("Number isn't prime")
        
    

"""
4 - Python Program to Check if a Number is an Armstrong Number ?
"""

def armstrong_number():
    # take input from user
    n = int(input('Enter a number'))
    
    # instialize sum
    sum = 0
    temp = n
    
    # calculate the length of digits
    le = len(str(n))
    
    
    while temp > 0:
        dig = temp % 10
        sum += dig ** le
        temp //=10
    
    # displat the result
    if n == sum:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")

    
    
    
    

if __name__ == '__main__':
    check_prime_no()


    
