# set={1,2,3}
#
# #add
# set.add(4)
# print(set)
#
# #update
# set.update([5,6,7])
# print(set)
#
# set.update({3,8,9})
# print(set)


#union : combine unique element
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A.union(B))

#intersection : restrun only common value
print(A&B)
print(A.intersection(B))

#difference
print(A-B)
print(A.difference(B))

#symmetric diffrence
print(A^B)
print(A.symmetric_difference(B))