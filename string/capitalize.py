# capitalize first letter of all words in sentence

s = input()
for x in s.split(' '):
    s = s.replace(x, x.capitalize())
print(s)