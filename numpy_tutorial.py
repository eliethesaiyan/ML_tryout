#Numpy exploration with Python 2.7
from math import sqrt

#1. Numbers
title="Number title"
print title
x=3
b=3.4
#print type of number
print type(x)
print type(b)
#exponential
print x**b
#print multi arguments
print x,b,x+1,b+1,x**b

#2. Strings literral
title="String litteral"
hello='Hello'
world="World"
print hello+" "+world

#string format styling
formated='%s %s %d' %(hello,world,x)
print formated


#3. Lists
title="lists"
print title
nums=range(10)

print "Last element"
print nums[:-1]
print "Remove the last element"
nums.pop()
print nums

print "slice without including the first and last element"
print nums[1:-1]

#4. Loops
title="looping through containers"
print title
for num in nums:
    print num

print "Access list element using indexes in for loop"

for idx,val in enumerate(nums):
    print "%d %d" %(idx+1,val)

print "Creating list by comprehensions using the squares "

squares=[]
for x in nums:
    squares.append(x**2)
print squares

print "even square Same list created using comprehensions"
even_squares=[x**2 for x in nums]

#5. Dictionaries

title="Using dictionaries"
print title
d={"cat":"miaou","dog":"Barks","Lion":"Roars"}

print d["cat"]
print "dog" in d
print "Add new element in the dictionary using key :'fish':swims"
d["fish"]="swims"
print d
print d.get("Monkey","N/A")
print "Looping in dictionaries"

for animal in d:
    print d[animal]

print "Access dictionary with key values using iteritems()"

for animal,speech in d.iteritems():
    print "a %s %s."%(animal,speech)


print "Dictionary with comprehensions created from nums list"
print  nums
even_num_to_square={x:x**2 for  x in nums if x%2==0}
print even_num_to_square

#5. Sets
title="Working with sets"

print title
print "Square roots from nums list using comprehension"
sq_root={sqrt(x) for x in nums}
print sq_root

#6 tuples

title="Working with tuples"
print title
tup={(x,x*2): x for x in nums} 
print tup
t=(12,24)
print type(t)
print tup[(5,10)]

#7. Functions
title="Working with functions"
def sign(x):
    if x>0:
       print "The number is positive"
    elif x<0:
       print "The number is negative"
    else:
       print "Zero was given as argument"


for x in [-1,0,1]:
    print sign(x)

print "Function with default arguments"

def hello(name,loud=False):
    if loud:
       print "Hello %s!" %name.upper()
    else:
       print "Hello %s!" %name

print hello("Bob")
print hello ("Bob",True)


#8. Classes
title="Working with classes"

class Greeter(object):
      
      #Constructor
      def __init__(self,name):
          self.name=name
     

      def greet(self,loud=False):
          if loud:
             print "Hello %s "% self.name.upper()
          else:
             print "Hello %s "% self.name

g=Greeter("Fred")
print g.greet(True)
print g.greet()
              
          
