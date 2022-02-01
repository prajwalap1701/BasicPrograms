txt = "I love apples, apple are my favorite fruit"
txt_list = txt.split(' ')
for word in txt_list:
    print(word+" : "+str(txt.count(word)))
