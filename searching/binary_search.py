def binary_search(arr, elem):
    
    first = 0
    last = len(arr) - 1
    found = False
    
    while first <= last and not found:
        
        mid = (first+last)/2
        
        if arr[mid] == elem:
            found = True
        else:
            if elem < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found
                
    

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    result = binary_search(arr, 7)
    print(result)