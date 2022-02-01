# Given the names and grades for each student in a class of  students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their
# names alphabetically and print each name on a new line.


li = []
score_list = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    li.append([name, score])
    score_list.append(score)
li.sort()
score_list = list(set(score_list))
score_list.sort()
sec_marks = score_list[1]
for st in li:
    if sec_marks == st[1]:
        print(st[0])
