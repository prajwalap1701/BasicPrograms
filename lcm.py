def lcm(x, y):
    lcm = 0
    if x > y:
        gnum = x
    else:
        gnum = y

    for i in range(gnum,9999, gnum):
        if i % x == 0 and i % y ==0:
            lcm = i
            break
    return lcm

print(lcm(12, 34))