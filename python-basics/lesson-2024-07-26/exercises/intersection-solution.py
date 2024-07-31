list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def intersection(lst1, lst2):
    result = set(lst1).intersection(set(lst2))
    return list(result)

print(intersection(list_1, list_2))
