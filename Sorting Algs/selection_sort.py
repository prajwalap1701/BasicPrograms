def selection_sort(list1):
    # we dont need to sort last element as it will be sorted automatically
    for i in range(0, len(list1)-1):
        min_value_index = i

        for j in range(i+1, len(list1)):
            if list1[j] < list1[min_value_index]:
                min_value_index = j

        if min_value_index != i:
            # swap
            list1[min_value_index], list1[i] = list1[i], list1[min_value_index]
            print(list1)

    return list1

print(selection_sort([45, 56,23,5,89,12,4]))