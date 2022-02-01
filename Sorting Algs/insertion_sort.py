def insertion_sort(list1):
    for index in range(1, len(list1)):
        pos = index
        cur_ele = list1[index]
        while cur_ele < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos = pos - 1
        list1[pos] = cur_ele
    return list1

print(insertion_sort([12, 1, 7, 93, 23, 43]))
