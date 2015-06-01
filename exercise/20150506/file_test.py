poem = """Programming is fun
when the work is done
if your wanna make your work also fun;
use python!
"""

f = file("poem.txt",'w')

f.write(poem)
f.close()

f = file("poem.txt")

while 1:
    line = f.read()

    if len(line) == 0:
        break
    print line

f.close()
