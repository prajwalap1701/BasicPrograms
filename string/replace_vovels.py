# replace vowels in string with *

vowels_list = ['a', 'e', 'i', 'o', 'u']
inp_str = input("Enter a string: ")

str_list = list(inp_str)

for c in str_list:
    if c in vowels_list:
        v_index = str_list.index(c)
        str_list[v_index] = '*'

print("".join(str_list))