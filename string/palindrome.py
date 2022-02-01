# palindrome or not

inp_str = input("Enter a string: ")

if inp_str == inp_str[::-1]:
    print(f'{inp_str} is palindrome')
else:
    print(f'{inp_str} is not a palindrome')