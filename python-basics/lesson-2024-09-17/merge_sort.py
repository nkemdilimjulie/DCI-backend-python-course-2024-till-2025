
# Merge sort

num_list = [300, 7, 55, 220, 4, 77, 12, 2, 444, 88]

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid_idx = len(lst) // 2

    left_lst = lst[:mid_idx]
    right_lst = lst[mid_idx:]

    left = merge_sort(left_lst)
    right = merge_sort(right_lst)

    return merge(left, right)


def merge(left, right):

    i = 0
    j = 0

    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


print(f'Original list: {num_list}')
print(f'Sorted list: {merge_sort(num_list)}')

        












    







