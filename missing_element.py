"""
given two arrays, find the missing element in the second array 
"""

def missing_element(arr1, arr2):
    
    # sort two arrays
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            # print(num1)
            return num1
    return arr1
    
"""
solution2:- by performing a very clever trick, we can achieve linear time and constant space complexity
            without any problem , here it is instialize a variable to 0, then XOR every element in the 
            first and second arrays with that variable, in the end value of the variable is the result
"""

def missing_element_v2(arr1, arr2):
    result = 0
    
    # perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
    return result


        
if __name__ == '__main__':
    arr1 = [5,5,7,7,6,6]
    arr2 = [5,7,7,6,5]
    result = missing_element_v2(arr1,arr2)
    print(result, 'result is:--')
    