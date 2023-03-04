def merge_sort(array):
    if len(array) > 1:
        center = len(array) // 2

        left = array[:center]
        right = array[center:]

        merge_sort(left)
        merge_sort(right)

        l = r = k = 0
        while (l < len(left) and r < len(right)):
            if(left[l] < right[r]):  
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1
  
        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1


array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
print("Before Sorting : {}".format(array))

merge_sort(array)
print("After Sorting  : {}".format(array))
