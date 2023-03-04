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

array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
array.sort()
print(binary_search(array , 100)) # print False
print(binary_search(array , 0)) # print False
print(binary_search(array , 12)) # print True