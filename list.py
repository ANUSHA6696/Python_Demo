#list functions 

l1=["apple","banana",1,5,True]
#last item
item=l1[-1]

#printing list values
for i in l1:
    print(i)

#length of list
print(len(l1))

#append
l1.append("lemon")

#insert to a particular index
l1.insert(1,23)

#To delete the last element from the list
l1.pop()

#to remove a particular element 
l1.remove(5)

#to reverse the list
l1.reverse()

#delete all elements 
l1.clear()

#sort alphabetically or in ascending order
l1.sort()

l2=[1,2,3,4,5,6,7,8,9,0]

#slicing(start:stop:index)
a=l2[2:6:2]
#print(a)

#to copy, if the copy is modified then original is also modified
l3=l2

#instead use copy
l4=l2.copy()

#for creating a new list using existing list, ex from a list of numbers we can create a squared number list
l5=[1,2,3,4,5]
l6=[i*i for i in l5]
print(l6)

#print(l1)
