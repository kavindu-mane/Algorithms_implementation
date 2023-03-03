def bubble_sort(arr):
    iterations = len(arr) - 1
    for i in range(iterations):
        sorted_finish = True
        for k in range(iterations - i):
            if (arr[k] > arr[k+1]):
                sorted_finish = False
                arr[k] , arr[k+1] = arr[k + 1] , arr[k]

        if(sorted_finish): # this condition helps to use bubble sort with time efficient through stopping running unnecessary iterations.
            break
    return arr

print(bubble_sort([10,2,5,7,8,9,12,13,2,-1]))