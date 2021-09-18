
def recursive_search(arr, elem):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)/2
        
        if elem == arr[mid]:
            return True
        else:
            if elem < arr[mid]:
                return recursive_search(arr[:mid], elem)
            else:
                return recursive_search(arr[mid+1:], elem)
    
            

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    result = recursive_search(arr, 7)
    print(result)
    