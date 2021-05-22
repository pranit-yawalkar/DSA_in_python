def merge_sort(arr, key, descending=False):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, key, descending)
    merge_sort(right, key, descending)
    merge_two_sorted_arrays(left, right, arr, key, descending)

def merge_two_sorted_arrays(a, b, arr, key, descending=False):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    if descending:
        while i < len_a and j < len_b:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1
    else:
        while i < len_a and j < len_b:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


if __name__ == "__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_sort(elements, key='time_hours', descending=True)
    merge_sort(elements, key='name')
    print(elements)

#OR

# def merge_sort(elements, key, descending=False):
#     size = len(elements)

#     if size == 1:
#         return elements

#     left_list = merge_sort(elements[0:size//2], key, descending)
#     right_list = merge_sort(elements[size//2:], key, descending)
#     sorted_list = merge(left_list, right_list, key, descending)

#     return sorted_list

    
# def merge(left_list, right_list, key, descending=False):
#     merged = []
#     if descending:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] >= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))

#     else:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] <= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))

#     merged.extend(left_list)
#     merged.extend(right_list)
#     return merged

# if __name__ == '__main__':
#     elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]

#     sorted_list = merge_sort(elements, key='time_hours', descending=True)
#     print(sorted_list)