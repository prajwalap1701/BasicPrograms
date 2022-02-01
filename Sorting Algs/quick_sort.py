def quick_sort (list1):
    length = len(list1)
    if length <= 1:
        return list1
    else:
        pivot = list1.pop()

    greater_li = []
    lower_li = []

    for num in list1:
        if num < pivot:
            lower_li.append(num)
        elif num > pivot:
            greater_li.append(num)

    return quick_sort(lower_li) + [pivot] + quick_sort(greater_li)

print(quick_sort([10, 8, 4, 12, 6, 15]))
