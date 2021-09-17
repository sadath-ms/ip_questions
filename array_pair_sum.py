# given an integer array, output all unique pairs that sum up with a specific value k

# input pair_sum([1,3,2,2],4)
#                array integrt k

def array_pair_sum(arr, k):
    
    if len(arr) < 2:
        return False
    
    # Sets for tracking 
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return '\n'.join(map(str, list(output)))

if __name__ == '__main__':
    result = array_pair_sum([1,3,2,2], 4)
    print(result)
    

