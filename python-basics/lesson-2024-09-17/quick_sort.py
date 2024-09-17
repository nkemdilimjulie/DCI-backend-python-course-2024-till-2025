
# Quick sort


num_list = [20, 100, 2, 33, 8, 40, 7, 55, 8, 21]


def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]

        left_lst = [x for x in lst if x < pivot]
        right_lst = [x for x in lst if x > pivot]
        middle_lst = [x for x in lst if x == pivot]

        return quick_sort(left_lst) + middle_lst + quick_sort(right_lst)


print(f'Original list: {num_list}')
print(f'Sorted list: {quick_sort(num_list)}')


# Reverse sort

# def quick_sort(lst):

#     if len(lst) <= 1:
#         return lst
#     else:
#         pivot = lst[len(lst) // 2]

#         left_lst = [x for x in lst if x > pivot]
#         right_lst = [x for x in lst if x < pivot]
#         middle_lst = [x for x in lst if x == pivot]

#         return quick_sort(left_lst) + middle_lst + quick_sort(right_lst)


# print(f'Original list: {num_list}')
# print(f'Reversed list: {quick_sort(num_list)}')


# Reverse sort

# def quick_sort(lst):

#     if len(lst) <= 1:
#         return lst
#     else:
#         pivot = lst[len(lst) // 2]

#         left_lst = [x for x in lst if x < pivot]
#         right_lst = [x for x in lst if x > pivot]
#         middle_lst = [x for x in lst if x == pivot]

#         return quick_sort(right_lst) + middle_lst + quick_sort(left_lst)


# print(f'Original list: {num_list}')
# print(f'Sorted list: {quick_sort(num_list)}')
