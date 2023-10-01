def binary_search(array ,search_term):
    mid = len(array) // 2
    if(array[mid] == search_term):
        return True
    elif array[mid] != search_term and mid == 1:
        return False
    elif array[mid] > search_term:
        return binary_search(array[:mid] ,search_term)
    elif array[mid] < search_term:
        return binary_search(array[mid + 1:] ,search_term)

array = [ 1 , 2, 5 , 7 , 20 , 25 , 32, 37 , 40 , 42 , 50 , 61 , 63 ,75]
array.sort()
print(binary_search(array , 100)) # print False
print(binary_search(array , 42)) # print True
print(binary_search(array , 75)) # print True
