#Numpy exploration with Python 2.7
from math import sqrt
import numpy as np

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


#9 Numpy datatypes

title="Working with Numpy datatypes"
print "Rank one array has a structure of a list"
a=np.array([1,2,3])
print a
print "Shape"
print a.shape
print "First element is the number of elements counting from the outmost []"
b=np.array([[2,3,4],[5,6,8]])
print b
print "Shape"
print b.shape
print "array is indexed from zero,b[0,2] is 4,b[1,0] is 5"
print b[0,2]
print b[1,0]

#10 initializing numpy arrays
title="Initializing numpy array"
print "Initializing with zeros(2,2)"
a=np.zeros((2,2))
print a

print "initializing with ones(4,4)"
print np.ones((4,4))

print "initialzing with a default value with full((2,2),3)"
print np.full((2,2),3)

print "Creating identity matrix of dimension 3x3"
print np.eye(3)

print "Initializing with random values of an array of 3 elements with 4 random values each"

print np.random.random((3,4))
#11 index array
title="Indexing array and slicing them"
print title
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print a
b=a[:2,1:2]
print "sliced b=a[:2,1:3]"
print b

print a[0,1]
print "Change the data of a slice of an array will eventually lead to the change of the original array b[0,0]=77 will change a[0,1]"
b[0,0]=77
print "b[0,0]"
print b[0,0]
print "a[0,1]"
print a[0,1]
print "Changed a"
print a
print "the second second row alone of a print row_1=a[1,:] which will be array of shape(4,) with rank 1"
row_1=a[1,:]
print row_1,row_1.shape
print "Print selection from row 1 until 2 but doesn't include 2 row,row_2=[1:2,:] which keeps the shape of (1 row,3 columns)"
row_2=a[1:2,:]
print row_2,row_2.shape
print "one column of shape (,3) but since is rank one it becomes same as row(3,)"
col_1=a[:,1]
print col_1,col_1.shape
print "columns from 1 to 2 indexes wihout including 2 of all rows with shape(3,1)"
col_2=a[:,1:2]
print col_2,col_2.shape

#12 indexing using integer
title="Indexing using integers"
c=np.array([[1,2],[3,4],[5,6]])
print "Indexing with integer,usually the first index list describe the first row coordinates of an element and the second describe the columns cooridnate of element to be selected c[[0,1,2],[0,1,0]]"
print c[[0,1,2],[0,1,0]]
print np.array([c[0,0],c[1,1],c[2,0]])
print "Indexing with integer one array of column indexes desired to change the rows"
d=np.array([1,0])
c[np.arange(2),d]+=10
print c

#13 indexing using boolean

title="Indexing using boolean values"
print title
bool_idx=(c>2)
print bool_idx

#14 numpy datatypes
title="specifying datatypes of arrays"
print title
d=np.array([1,2,7])
print d.dtype
print d.shape
print "Can be specified on creation"
d=np.array([1,2,3],dtype=np.float64)
print d
#15 numpy array  maths"
title="maths with numpy"
print title
x=np.array([[1,2,4],[1,2,4],[1,4,4]],dtype=np.float64)
y=np.array([[4,2,5],[1,2,3],[1,2,3]],dtype=np.float64)

print x+y
print np.add(x,y)
print np.subtract(x,y)

v=np.array([9,10])
w=np.array([11,12])
print "dot production of "
print v
print v.dot(w)
print "sum of all element using np.sum(x)"
print np.sum(x)
print "Sum all elements on rows[x,axis=0]"
print np.sum(x,0)
print "Sum all elements on columns[x,axis=1]"
print np.sum(x,1)

print "Making transposee of y"
print y
print y.T
print "Broadcasting :Adding a vector to each row of the array"
broad=np.empty_like(x)
for i  in range(2):
    print "original"
    broad[i,:]=x[i,:]+d
    print x[i,:]
    print "broadcasted"
    print broad[i,:]
   


print "Tiling "

xx=np.tile(d,(3,1))

print xx

print xx+x

print "reshaping"

v=np.array([1,2,3])
w=np.array([4,5])
print "V and w initial content"
print v,w

print "After reshape of v"
print np.reshape(v,(3,1))*w
z=np.array([[1,2,3],[2,3,4]])

print (z.T+w).T
print "original z"
print z

print "broadcasted z"
print z+np.reshape(w,(2,1))































              
          
