inp = input('Enter numbers to sort: ')
list1 = inp.split(' ')
print(f'List before sorting: {list1}')

for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] < list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

print(f'List after sorting: {list1}')
