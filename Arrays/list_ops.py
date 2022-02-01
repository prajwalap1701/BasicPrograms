
n = int(input())
li = []

for i in range(1,n+1):
    inp = input()
    print(inp)
    inp_list = inp.split(' ')
    if inp_list[0] == 'insert':
        li.insert(int(inp_list[1]), int(inp_list[2]))
    elif inp_list[0] == 'append':
        li.append(int(inp_list[1]))
    elif inp_list[0] == 'remove':
        li.remove(int(inp_list[1]))
    elif inp_list[0] == 'pop':
        li.pop()
    elif inp_list[0] == 'sort':
        li.sort()
    elif inp_list[0] == 'reverse':
        li.sort(reverse= True)
    elif inp_list[0] == 'print':
        print(li)