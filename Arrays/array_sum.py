# You are given two numbers represented as integer arrays A and B, where each digit is an element.
#
# You have to return an array which representing the sum of the two given numbers.
#
# The last element denotes the least significant bit, and the first element denotes the most significant bit.

A = [9,6,5,9]
B = [4,7,2,9]
s_num1 = ''
s_num2 = ''

for e1 in A:
    s_num1 += str(e1)
for e2 in B:
    s_num2 += str(e2)

sum = int(s_num1) + int(s_num2)
sum_arr = []
for s in str(sum):
    sum_arr.append(int(s))
print(sum_arr)


# class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     # @return a list of integers
#     def addArrays(self, A, B):
#         A.reverse()
#         B.reverse()
#         C = []
#         carry = 0
#         i = 0
#         n = min(len(A), len(B))
#         while i < n:
#             x = carry + A[i] + B[i]
#             C.append(x % 10)
#             carry = x // 10
#             i += 1
#
#         while i < len(A):
#             x = carry + A[i]
#             C.append(x % 10)
#             carry = x // 10
#             i += 1
#
#         while i < len(B):
#             x = carry + B[i]
#             C.append(x % 10)
#             carry = x // 10
#             i += 1
#
#         while carry > 0:
#             C.append(carry % 10)
#             carry = carry // 10
#
#         C.reverse()
#
#         return C