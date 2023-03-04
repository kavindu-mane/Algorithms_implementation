def selection_sort(array):
    for i in range(1,len(array)):
        min_index = i - 1
        for k in range(i , len(array)):
            if array[min_index] > array[k]:
                min_index = k

        array[i - 1] , array[min_index] = array[min_index] , array[i - 1]


array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
print("Before Sorting : {}".format(array))

selection_sort(array)
print("After Sorting  : {}".format(array))
