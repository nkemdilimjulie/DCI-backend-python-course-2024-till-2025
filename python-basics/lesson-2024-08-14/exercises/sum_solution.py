dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}


def multiply_two(d1, d2):
    empty_list = []

    for i in d1:
        m = d1[i] * d2[i]
        empty_list.append(m)
    
    print(empty_list)
    
    return sum(empty_list)

print(multiply_two(dict1, dict2))
