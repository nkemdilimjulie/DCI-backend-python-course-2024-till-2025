# TODO implement mergesort

def mergesort(lst: list, left=0, right=-1) -> list:
    
    if right == -1:
        right = len(lst) -1
        
    if right > left:
        middle = int(left + (right - left) // 2)
        
        # mergesort both halves
        mergesort(lst, left, middle)
        mergesort(lst, middle + 1, right)
        
        # merge the halves
        merge(lst, left, middle, right)
    
    return lst


def merge(lst, left, middle, right):
    
    n1 = middle - left + 1
    n2 = right - middle
    
    # create temp lists
    left_temp = [0] * n1
    right_temp = [0] * n2
    
    # copy data to temp lists left & right
    for i in range(0, n1):
        left_temp[i] = lst[left + i]
    
    for j in range(0, n2):
        right_temp[j] = lst[middle + 1 +j]
    
    # merge the temp lists back
    
    # initial index of first sublist
    i = 0
    # initial index of second sublist
    j = 0
    # initial index of merged sublist
    k = left
    
    while i < n1 and j < n2:
        if left_temp[i] <= right_temp[j]:
            lst[k] = left_temp[i]
            i += 1
        else:
            lst[k] = right_temp[j]
            j += 1
        k += 1
    
    # copy remaining elements of left, if there are any
    while i < n1:
        lst[k] = left_temp[i]
        i += 1
        k += 1
    
    # copy remaining elements of right, if there are any
    while j < n2:
        lst[k] = right_temp[j]
        j += 1
        k += 1
