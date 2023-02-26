# Kruskal's Algorithm 
def kruskals(paths):
    visited = []
    weight = 0
    
    for a , b , c in paths:
        if(a not in visited or b not in visited):
            weight += int(c)
            if a not in visited: visited.append(a)
            if b not in visited: visited.append(b)
    return weight

path_count = int(input("Enter edge count : "))
paths = []
n = 0
for _ in range(path_count):
    n += 1
    paths.append(input("Enter edge {} : ".format(n)).split(" "))
    
paths = sorted(paths , key = lambda x : int(x[2]))
print("Minimum cost : {}".format(kruskals(paths)))

#Sample Input
#7
#A B 5
#B E 10
#E D 10
#E C 30
#D C 20
#D B 35
#C A 10
