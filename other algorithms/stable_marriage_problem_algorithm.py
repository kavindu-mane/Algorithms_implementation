def print_couples(couples):
    for b , g in couples.items():
        print("{} and {}".format(b ,g))

def stable_marriage(boys , girls):
    mached_couple = {
        "James": None,
        "William": None,
        "Daniel": None,
        "John": None
    }

    mached_couple_girl = {
        "Emma": None,
        "Sophia": None,
        "Ellie": None,
        "Maya": None
    }

    like_level = {
        "James": 0,
        "William": 0,
        "Daniel": 0,
        "John": 0
    }

    while None in mached_couple.values():
        for key in  mached_couple.keys():
            if mached_couple[key] is None:

                next_girl = boys[key][like_level[key]]
                current_boy_name = mached_couple_girl[next_girl]
                set_couple = False
                next_girl_like_order = girls[next_girl]

                if(current_boy_name is None):

                    set_couple = True

                elif  next_girl_like_order.index(current_boy_name) >  next_girl_like_order.index(key):
                    
                    set_couple = True
                    mached_couple[current_boy_name] = None
                
                if set_couple:
                    mached_couple[key] = next_girl
                    mached_couple_girl[next_girl] = key

                like_level[key] += 1
    print_couples(mached_couple)


boys = {
    "James": ["Maya","Sophia","Ellie","Emma"],
    "William": ["Maya","Sophia","Emma","Ellie"],
    "Daniel": ["Sophia","Emma","Maya","Ellie"],
    "John": ["Sophia","Maya","Ellie","Emma"]
}

girls = {
    "Emma": ["John","William","Daniel","James"],
    "Sophia": ["William","James","John","Daniel"],
    "Ellie": ["James","Daniel","John","William"],
    "Maya": ["John","James","Daniel","William"]
}

stable_marriage(boys , girls)
# Assume that all time boy will ask out and girl never do it.