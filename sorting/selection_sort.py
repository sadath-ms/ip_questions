"""
SELECTION SORT:-
 
selection sort improves on the bubble sort by making only one exchange for every pass through the list.
in order to do this, a selection sort looks for the largest value as it makes a pass and, after completing
the pass, place it in a proper location,

as with a bubble sort, after the first pass , the largest item is in correct place , after the second pass
, the next largest is in place,this process continues and requires n-1 passes to sort n iteams, since the 
final iteam must be the place after the (n-1)st pass

"""

def selection_sort(arr):
    
    # for every slots in an array
    for fillslot in range(len(arr)-1,0,-1):
        postion_of_max = 0
        # for every set of 0 to fillslot+1
        for location in range(1, fillslot+1):
            # set maximum location
            if arr[location] > arr[postion_of_max]:
                postion_of_max = location
        
        temp = arr[fillslot]
        arr[fillslot] = arr[postion_of_max]
        arr[postion_of_max] = temp

    return arr

if __name__ == '__main__':
    arr = [3,5,2]
    result = selection_sort(arr)
    print(result)
    