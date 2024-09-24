# TODO implement bubble sort

def bubblesort(list):
  swaps = False
  for i in range(len(list) -1):
    if list[i] > list[i+1]:
      list[i], list[i+1] = list[i+1], list[i]
      swaps = True

  if swaps:
    bubblesort(list)
    return list
