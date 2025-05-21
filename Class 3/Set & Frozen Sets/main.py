# SETS
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}

print("Union of set1 and set2: ",set1 | set2)
print("Intersection of set1 and set2: ",set1 & set2)

print("Set 1: ",set1)
set1.add(6)
print("After adding 6: ",set1)
set1.remove(6)
print("After removing 6: ",set1)

# Frozen Sets
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen set: ",frozen_set)
# frozen_set.add(6) # This will raise an error because frozen sets are immutable
