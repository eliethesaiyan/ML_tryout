#Numpy exploration with Python 2.7

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




