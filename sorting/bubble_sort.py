def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

if __name__ == '__main__':
    arr = [2,4,7,6,1,5]
    result = bubble_sort(arr)
    print(result)
    