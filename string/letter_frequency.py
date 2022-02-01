txt = "I love apples, apple are my favorite fruit"
char_set = set(txt)

for letter in char_set:
    print(f'{letter}: {txt.count(letter)}')