def seq_search_v1(arr, elem):
    for ele in arr:
        if ele == elem:
            return 'Found'
    return "Not Found"


def seq_search_v2(arr, elem):
    # searching for un order list 
    pos = 0
    while pos < len(arr):
        
        if arr(pos) == elem:
            return 'Found'
        pos += 1
        
    return "Not Found"
    

def seq_ordered_list(arr, elem):
    
    pos = 0
    found = stopped = False
    
    while pos < len(arr) and not stopped:
        if arr[pos] == elem:
            found = stopped = True
            
        else:
            # if arr[pos] > elem:
            #     stopped = True
            # else:
            pos +=1
    return found
            


if __name__ == '__main__':
    arr = [1,2,3,4]
    result = seq_ordered_list(arr, 7)
    print(result)
    