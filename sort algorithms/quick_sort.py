def partition(array , lb , ub):
    pivot = array[lb]
    start = lb + 1 
    end = ub

    while True:
        while start <= end and array[start] <= pivot:
            start += 1
        while start <= end and array[end] > pivot:
            end -= 1
        if start < end:
            array[start] , array[end] = array[end] , array[start]
        else:
            break
    array[lb] , array[end] = array[end] , array[lb]
    return end

def quick_sort(arry , start , end):
    if start >= end:
        return
    
    splitter = partition(arry , start , end)
    quick_sort(arry , start , splitter - 1)
    quick_sort(arry , splitter + 1 , end)

array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
# array = [10,6,11,8,12,2,9,15]
print("Before Sorting : {}".format(array))

quick_sort(array , 0 , len(array) -1)
print("After Sorting  : {}".format(array))
