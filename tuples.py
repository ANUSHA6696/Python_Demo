 #for objectsj that belong together
 #one element inside a () is a string so it needs to be followed by a ,
 
mytuple= tuple([1,"name","jim",14])
print(mytuple[1])

#to check if a value is within a tuple
if "name" in mytuple:
    print("yes")
else:
    print("no")

#to check len of tuple
print(len(mytuple))

tuple2=(1,2,3,4,5,5,5,6)

#to find count of any particular value
print(tuple2.count(5))

#to find index of any value(in case of repeated gives first)
print(tuple2.index(2))

#to convert to list
l1=list(tuple2)
print(l1)

#slicing
a=tuple2[2:6]
print(a)

#unpacking a tuple
b ="jim",32,"salesman"
name,age,role = b #no of elements should be the same
print(name)

#multiple elements can be unpacked using *
i1,i2,*i3 = tuple2 #here i1,i2 is the first and second element whereas i3 is all other elements to a list
print(i3)

#a size of list in bytes is larger than tuple even after having same elements
#efficient to iterate a tuple compared to a tuple




