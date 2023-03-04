def linear_search(array , search_term):
    for value in array:
        if value == search_term:
            return True
    return False

array = [ 2, 5 , 1 , 2 , 20 , 15 , 12, 3 , 4 , 2 , 50 , 21 , 23 ,35]
print(linear_search(array , 100)) # print False
print(linear_search(array , 12)) # print True