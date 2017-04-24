#Union of the sets A and B
def union(a,b):
    ret = [x for x in a if x not in b]
    ret.extend(b)
    return ret

#Intersection of the sets A and B is the set of all objects that are members of both A and B. The intersection of {1, 2, 3} and{2, 3, 4} is the set {2, 3} .
def intersection(a,b):
    ret = [x for x in a if x in b]
    return ret

#Set difference of U and A, denoted U \ A, is the set of all members of U that are not members of A. The set difference {1, 2, 3} \ {2, 3, 4} is {1}, while, conversely, the set difference {2, 3, 4} \ {1, 2, 3} is {4} . When A is a subset of U, the set difference U \ A is also called the complement of A in U. In this case, if the choice of U is clear from the context, the notation Ac is sometimes used instead of U \ A, particularly if U is a universal set as in the study of Venn diagrams.
def setDifference(a,b):
    ret = [x for x in a if x not in b]
    return ret

#Symmetric difference of sets A and B is the set of all objects that are a member of exactly one of A and B (elements which are in one of the sets, but not in both). For instance, for the sets {1, 2, 3} and {2, 3, 4} , the symmetric difference set is {1, 4} . It is the set difference of the union and the intersection, (A u B) \ (A n B) or (A \ B) u (B \ A).
def symmetricDifference(a,b):
    ret = setDifference(union(a,b),intersection(a,b))
    return ret

#Cartesian product of A and B, denoted A x B, is the set whose members are all possible ordered pairs (a, b) where a is a member of A and b is a member of B. The cartesian product of {1, 2} and {red, white} is {(1, red), (1, white), (2, red), (2, white)}.
def cartesianProduct(a,b):
    ret = [(x,y) for x in a for y in b]
    return ret

a = [1,2,3]
b = [2,3,4]
print union(a,b)
print intersection(a,b)
print setDifference(a,b)
print symmetricDifference(a,b)
print cartesianProduct(a,b)
