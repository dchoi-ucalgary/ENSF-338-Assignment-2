import sys
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    # to make it more efficient, we can 
    # check if the list is already sorted, 
    # This will not increase complexity, since 
    # O(n*logn) is greater than O(n).
    # This will also cause our 
    # best case scenario (already sorted)
    # to be O(n), which is better

    if low < high:
        sorted = 0
        if(all(arr[i] <= arr[i + 1] for i in range(len(arr)-1))):
            sorted = True

        if(sorted == False):
            pi = func2(arr, low, high)
            func1(arr, low, pi-1)
            func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high