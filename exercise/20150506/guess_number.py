import random
number = random.randint(1,20)

while 1:
        guess = int(raw_input("Enter a number"))

        if guess == number:
                print "Well Done"
                break
        elif guess > number:
                print "Bigger"
        else:
                print "Smaller"

print "number is " + str(number)


for i in range(1,10,3):
        continue
        print i
        
else:
        print "else"
