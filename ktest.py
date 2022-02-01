f = open("input.txt", "r+")
file_line = f.readline()
while file_line:
    temp = file_line.strip()
    if temp.isalnum() == False or temp.isalpha() == False:
        if int(temp) % 2 != 0:
            print(temp)
    file_line = f.readline()


# def process_list(sample_list):
#     sample_set = set(sample_list)
#     return list(sample_set)

# print(process_list(['navin', 3, 7, 'navin', 3]))


# def kth_highest(num_list, k):
#   num_list.sort(reverse = True)
#   k_highest_index = k - 1
#   return num_list[k_highest_index]
#
# print(kth_highest([7, 3, 22, 42, 6], 3))
#
# def secondlast(sample_str):
#   str_list = sample_str.split(',')
#   return str_list[-2]
# print(secondlast('Sales,Nashik,6 Feb 2020,233'))

# def process_list(mylist):
#     int_list = [x for x in mylist if isinstance(x, int)]
#     for num in int_list:
#         if num % 3 == 0 and num % 5 == 0:
#             i1 = int_list.index(num)
#             int_list[i1] = -3
#         elif num % 3 == 0:
#             i1 = int_list.index(num)
#             int_list[i1] = -1
#         elif num % 5 == 0:
#             i1 = int_list.index(num)
#             int_list[i1] = -2
#     return int_list
#
# print(process_list([1, 3, 5, 15, 22, 'b']))