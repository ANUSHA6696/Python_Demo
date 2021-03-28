#collection does not allow duplicates

l1=[1,2,2,2,3,3,4,2,5]
s=set(l1)
print(s)

s1=set("hello")
print(s1)

#empty set
s3=set() #else it is either tuple or dict

# to add
s3.add(1)

#delete same as list or dict

#union combining two sets without duplication
even= {0,2,4,6,8}
odd = {1,3,5,7,9}
prime={2,3,5,7}
u=odd.union(even)

print(u)

#intersection takes common elements in both sets
i=odd.intersection(prime)
print(i)

#to check elements that are not in one set
SetA={1,2,3,4,5}
SetB={5,6,7,8,9}
diff=SetA.difference(SetB) #gives elements from set b not in set a
print(diff)

#gives all elements not in both sets
diff2= SetB.symmetric_difference(SetA)

SetA.update(SetB) #adds elements in setb not in seta without duplication to set a

#same applies for all other types

#subset if all elements of set1 in set2
set1={1,2,3,4,5,6}
set2={1,2,3}
print(set1.issubset(set2)) #checks if all elements of set1 is  in set2 gives false but vice versa is true
print(set2.issuperset(set1)) #gives false as set2 does not contain all elemts of set1 but vice versa is true

#disjoint if both sets have null intersection
set3={4,5,6}
print(set2.isdisjoint(set3))

#copy is same as list
#frozenset is an immutable set


