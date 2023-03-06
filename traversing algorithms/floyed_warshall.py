def floyed_warshall(matrix , loops , vertex , indexes):
    for index in range(loops):
        center = vertex[index]

        for s in vertex:
            for e in vertex:
                if s != center and e != center:
                    s_index , e_index , c_index = indexes[s] , indexes[e] ,indexes[center]
                    direct_value = float(matrix[s_index][e_index])
                    checked_value = float(matrix[s_index][c_index]) + float(matrix[c_index][e_index])
                    matrix[s_index][e_index] = min(direct_value , checked_value)
    
    sorted(vertex)
    for node in vertex: print("\t {}".format(node),end="")

    for node_raw in vertex:
        print("\n{}".format(node_raw) , end ="")
        i_r = indexes[node_raw]

        for node_col in vertex:
            i_c = indexes[node_col]
            temp = matrix[i_r][i_c]
            val =  temp if temp == float('inf') else int(temp)
            print("\t {}".format(val) , end="")
    print("\n")


def create_matrix(paths):
    vertex = []
    indexes = {}
    index = 0

    for s , e ,w in paths:
        if s not in vertex: vertex.append(s)
        if e not in vertex: vertex.append(e)

        if s not in indexes.keys():
            indexes[s] = index
            index += 1
        if e not in indexes.keys():
            indexes[e] = index
            index += 1

    loops = len(vertex)
    matrix = [[(float('inf') if y != x else 0) for x in range(loops)] for y in range(loops)]

    for s , e ,w in paths:
        if s != e: matrix[indexes[s]][indexes[e]] = w
    
    floyed_warshall(matrix , loops , vertex , indexes)


path_count = int(input("Enter edge count : "))
paths = []
n = 0
for _ in range(path_count):
    n += 1
    paths.append(input("Enter edge {} : ".format(n)).split(" "))
create_matrix(paths)

# Sample input - 1
# 10
# A B 3
# A C 5
# C D 4
# D B 2
# B C 3
# E F 10
# F A 12
# F E 2
# E D 3
# B F 7

# Sample input - 1
# 5
# A B 3
# A C 5
# C D 4
# D B -2
# B C 3