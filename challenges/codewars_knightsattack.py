from collections import deque
import math

directions = ((-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1),(2,1),(1,2))

def tupleadd(x: tuple, y:tuple):
    return x[0] + y[0], x[1] + y[1]

def inbounds(c, l) -> bool: # returns True if the coordinate is inside the boundaries of the map
    if l >= c[0] >= 0 and l >= c[1] >= 0:
        return True
    return False

def distance(s: tuple, d) -> tuple():
    # Considering we`d like to know which direction to go from start to dest
    return d[0] - s[0], d[1] - s[1]

def reasonable_dirs(start, dest, l) -> tuple():
    """
    Creating a dictionary with vector distances between all possible directions and the destination
    Yielding one which is the closest
    """

    dist = distance(start, dest)

    distance_vectors = {direction: round(math.dist(direction, dist),2) for direction in directions}

    # Need to sort by the values
    distance_vectors = sorted(distance_vectors.items(), key=lambda kv: (kv[1], kv[0]))

    for d, v in distance_vectors:
        newcoord = start[0] + d[0], start[1] + d[1]
        if inbounds(newcoord, l):
            #print(f"yielding {v} step_vector as the distance is {dist}")
            yield d

def displays(start, dest, o, limit):

    for _ in range(limit + 2):
        print("=", end=' ')
    for i in range(0, limit + 2):
        for j in range(0, limit + 2):
            if (i,j) in o:
                print("X", end=' ')
            elif start[0] == i and start[1] == j:
                print("S", end=' ')
            elif dest[0] == i and dest[1] == j:
                print("D", end=' ')
            elif j == limit + 1:
                print("=", end=' ')
            else:
                print(" ", end=' ')
        print()
    for _ in range(limit + 2):
        print("=", end=' ')

def noobstacle(s: tuple, d: tuple, o: tuple) -> bool:
    """
    Takes a starting coord and a direction / step and tells if there is an obstacle in the way
    """
    dd = list(d)

    for _ in range(3):
        if tupleadd(s,dd) not in o:
            if dd[0] > 0: dd[0] -= 1
            elif dd[0] < 0: dd[0] += 1
            elif dd[1] < 0: dd[1] += 1
            elif dd[1] > 0: dd[1] -= 1
        else:
            return False

    return True

def targetreached(q: deque, dest: tuple):
    for path in q:
        if dest in path:
            return True
    return False


def attack(start, dest, obstacles):

    l = max(max(start), max(dest))
    displays(start, dest, obstacles, l)

    q = deque()
    initialpath = list()
    initialpath.append(start)
    q.append(initialpath.copy())

    while not targetreached(q, dest):
        #print(f"q: {q}")
        path_to_build_on = q.popleft() # current path we are building on like [(7,1)]
        for next_possible_coord in reasonable_dirs(path_to_build_on[-1], dest, l):
            newcoord = tuple((path_to_build_on[-1][0] + next_possible_coord[0], path_to_build_on[-1][1] + next_possible_coord[1]))
            # adding a knight-step to the current coord like (7,1) + (1,-2) == (8,-1)
            # Validate if we are not stepping on obstable / out of the map
            if noobstacle(path_to_build_on[-1], next_possible_coord, obstacles) and not targetreached(q, newcoord):
                path_to_build_on.append(newcoord)
                q.append(path_to_build_on.copy())
                # print(f"{newcoord} is a valid place to go from {path_to_build_on}, added to {q}")

    for q_item in q:
        if q_item[-1] == dest:
            return len(q_item) - 1




# print("(7, 1), (5, 2), ())) # 1", attack((7, 1), (5, 2), ())) # 1
# print("(7, 1), (3, 3), ())) # 2", attack((7, 1), (3, 3), ())) # 2
# print("(7, 6), (0, 5), ())) # 4", attack((7, 6), (0, 5), ())) # 4
# print("(7, 6), (2, 1), ())) # 4", attack((7, 6), (2, 1), ())) # 4
# print("(7, 6), (7, 6), ())) # 0", attack((7, 6), (7, 6), ())) # 0
# print("(7, 6), (7, 7), ())) # 3", attack((7, 6), (7, 7), ())) # 3
# print("(7, 7), (1, 0), ())) # 5", attack((7, 7), (1, 0), ())) # 5

# print(attack((7, 1), (3, 3), ((5, 1), (5, 2), (5, 0), (4, 2), (4, 4), (7, 5))), 4)
# print(attack((6, 7), (7, 7), ((5, 5), (5, 6), (5, 7), (8, 6), (6, 9), (9, 6), (7, 9), (4, 6))), 5)
# print(attack((7, 1), (3, 3), ((5, 2),)), 4)
print(attack((7, 1), (3, 3), ((5, 1), (5, 2), (5, 0), (4, 2), (4, 4), (7, 5), (4, 3), (7, 4), (3, 4), (3, 6), (4, 7), (6, 7), (6, 4), (3, 6),(4, 5))), 4)
# print(attack((7, 6), (7, 7), ((5, 5), (5, 6), (5, 7))), 3)
# print(attack((7, 1), (3, 3), ((5, 1), (5, 2), (5, 0), (4, 2), (4, 4), (7, 5), (4, 3), (7, 4), (3, 4), (3, 6), (4, 7), (6, 7), (6, 4), (3, 6),(4, 5), (4, 6), (5, 3), (7, 3))), 4)
# print(attack((7, 1), (3, 3), ((5, 0), (6, 3), (5, 2), (4, 2), (4, 4), (7, 5), (4, 3), (1, 3), (3, 4), (0, 3), (4, 7), (0, 5), (6, 4), (1, 7),(4, 5), (4, 6), (5, 3), (7, 3))), 4)
# print(attack((0, 0), (7, 7), ((5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (8, 6), (6, 9), (9, 6), (8, 5), (7, 9), (4, 6), (9, 8))), 8)

