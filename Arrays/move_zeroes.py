# Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

arr = [0, 4, 6, 2,7,0,2,1, 0, 5]

z_count = arr.count(0)

for i in range(z_count):
    arr.remove(0)
    arr.append(0)

print(arr)

