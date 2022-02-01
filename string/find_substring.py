# the user enters a string and a substring. You have to print the number of times that the substring occurs in the
# given string. String traversal will take place from left to right, not from right to left.


def count_substring(string, sub_string):
    ctr = 0
    end = False
    while end == False:
        last_index = string.find(sub_string)
        if last_index == -1:
            end == True
            break
        ctr += 1
        string = string[last_index+1 :]
    return ctr


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)