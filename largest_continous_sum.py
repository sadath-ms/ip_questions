"""
LARGEST CONTINOUS SUM 

problem:-
    Given an array of integers(positive and negitive), find the largest continous sum

"""

def largest_csum_v2(arr):
    
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum
    

if __name__ == '__main__':
    arr = [1,2,-1,3,4,10,10,-10,-25]
    result = largest_csum_v2(arr)
    print(result)
    