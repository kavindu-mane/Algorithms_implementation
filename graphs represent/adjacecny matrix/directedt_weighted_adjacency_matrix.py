def print_matrix(matrix , indexes):

    keys = sorted(indexes.keys())

    for key in keys:
        print("\t{}".format(key) , end = "")

    for i in keys:
        print("\n{}".format(i) , end = " ")
        for k in keys:
            print("\t{}".format(matrix[indexes[i]][indexes[k]]) , end = " ")

def create_matrix(data_set , vertices):

    matrix = [[0 for k in range(vertices)] for n in range(vertices)]
    indexes = {}
    current_key = 0

    for start , end , weight in data_set:
        
        if(start not in indexes.keys()):
            indexes[start] = current_key
            current_key += 1

        if(end not in indexes.keys()):
            indexes[end] = current_key
            current_key += 1

        s_index = indexes[start]
        e_index = indexes[end]

        matrix[s_index][e_index] = weight

    print_matrix(matrix , indexes)
    print("\n")

# Example - 1 
create_matrix([["A" , "B" , 10] ,
                ["A" , "C" , 20] , 
                ["B" , "E" , 12] ,
                ["B" , "D" , 5 ],
                ["E" , "D" , 3] ,
                ["D" , "C" , 16]] , 5)

# Example - 2
create_matrix([[1,2,7] ,
               [1,3,9] ,
               [2,0,1] ,
               [2,4,11] ,
               [0,4,17] ,
               [4,3,19]] , 5)