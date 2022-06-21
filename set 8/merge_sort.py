def merge(a, b):
    result = []
    a_index = 0
    b_index = 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] > b[b_index]:
            result.append(b[b_index])
            b_index += 1
        else:
            result.append(a[a_index])
            a_index += 1
    if a_index < len(a):
        while a_index < len(a):
            result.append(a[a_index])
            a_index += 1
    else:
        while b_index < len(b):
            result.append(b[b_index])
            b_index += 1
    return result


def merge_sort(input_lst):
    if len(input_lst) > 1:
        left_half = []
        right_half = []
        middle = len(input_lst) / 2
        count = 0
        while count < middle:
            left_half.append(input_lst[count])
            count += 1
        while count < len(input_lst):
            right_half.append(input_lst[count])
            count += 1
    else:
        return input_lst
    result = merge(merge_sort(left_half), merge_sort(right_half))
    return result