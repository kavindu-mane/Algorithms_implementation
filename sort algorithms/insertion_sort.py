def insertion_sort(array):
    for i in range(1 , len(array)):
        tested = array[i]
        for k in range(i - 1 , -1 , -1):
            if(tested < array[k]):
                array[k] , array[k + 1] = array[k + 1] , array[k]
            else:
                break


array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
print("Before Sorting : {}".format(array))

insertion_sort(array)
print("After Sorting  : {}".format(array))
