class Person:
        population = 0

        def __init__(self,name):
                self.name = name

                print '(initializing %s)' %self.name

                Person.population += 1

        def __del__(self):
                """I am dying"""
                print "%s says bye." % self.name

                Person.population -=1
                if Person.population == 0:
                        print "I am the last one"
                else:
                        print "There are still %d people left."%Person.population

        def sayHi(self):
                """Greeting the person."""
                print "Hi,my name is %s."%self.name

        def howMany(self):
                """prints the current population."""
                if Person.population == 1:
                        print "I am the only person here"
                else:
                        print "we have %d persons here"%Person.population

class civilian(Person):
        def __init__(self,name,age,address):
                Person.__init__(self,name)
                self.age= age
                self.address = address
        def __del__(self):
                print "%s have been excuted"%self.name
        def tell(self):
                Person.sayHi(self)
                print 'My age is %d'%self.age, 'and my address is %s'%self.address
class 
class police(Person,civilian):
        def __init__()

s = Person("Swaroop")
s.sayHi()
s.howMany()

k = Person("Adul")
k.sayHi()
k.howMany()

s.sayHi()
s.howMany()


c = civilian("Chenye",23,'In heart?')
c.tell()
