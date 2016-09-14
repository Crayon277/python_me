students = []
n = int(raw_input())
for i in range(n):
    student=[]
    name = raw_input()
    grade = float(raw_input())
    student.append(name)
    student.append(grade)
    students.append(student)
students.sort()
wanted = []
lower = students.pop(0)
while 1:
    next_s = students.pop(0)
    if lower[1] == next_s[1]:
        pass
    else:
        break
wanted.append(next_s)
while 1:
    try:
        want_in = students.pop(0)
        if next_s[1] == want_in[1]:
            wanted.append(want_in)
        else:
            break
    except IndexError:
        break
for item in wanted:
    print item[0]
