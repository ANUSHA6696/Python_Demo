#contains key value pair

#dictionary can be configured in two ways
mydict={"name":"abc","age":24,"city":"Loughborough"}
print(mydict)

mydict2=dict(name="xyz",age=25,city="london",email="abc@xyz.com")
print(mydict2)

# to get value
value= mydict["age"]
print(value)

#to assign a new key value pair
mydict["role"]="student"
print(mydict)

#value can be overwritten

#to delete a key value there are two ways
#del mydict["age"]

#mydict2.pop("name")

#to remove last item
#mydict.popitem()

#to get keys from dict
for key in mydict2.keys():
    print(key)

#to get values
for value in mydict2.values():
    print(value)

for key,value in mydict.items():
    print(key,value)

#if we copy in the below way, if copy is modified, original also gets modified
mydict_cpy=mydict #they point to same dict in memory

#betterway to do is
mydict2_cpy=mydict2.copy()
mydict_cpy2=dict(mydict)

#to merge two dictionaries
mydict.update(mydict2) #adds keys not in mydict only
print(mydict)

#tuples can be used as key but not a list