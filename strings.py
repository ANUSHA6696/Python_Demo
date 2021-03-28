#ordered and immutable single or double quotes
#"""""" is for multi lines or documentation. it can also use \
#slicing is also used by using index as substring
#[::1] takes every character and [::2] takes every second character
#[::-1] reverses the string

from timeit import default_timer 
#to time any function or the time taken by a method

s1="hello"
s2="greetings"
s3=s1+s2 #concatination

#iteration
for i in s1:
    print(i)

#to remove white space
str1="       remove        "
str1=str1.strip() #since string is immutable doing it without assignment will give an error

s1.startswith("h") #checks if it is started with

print(s1.find('o')) #gives first index of o
print(s1.find('lo')) #gives index of lo

#part of word can be replaced
s1.replace('hello','world')
print(s1)

str3='how are you ?'
list1=str3.split() #splits by spaces by default, delimitor can be changed depending on the string
print(list1)

# converting a list back to a string
#DO NOT USE FOR LOOP TO READ FROM A LIST TO STRING AS THE TIME USED WILL BE O(N) INSTEAD BY USING JOIN IT WOULD BE O(1)
start= default_timer()
new_str= ' '.join(list1) #what is between the '' would be inserted between two elements from list to string
stop= default_timer()
print(stop - start)

new_str1=''
start1= default_timer()
for i in list1:
    new_str1 +=i
stop1= default_timer()
print(stop1-start1)

#formatting a string using %
var= 'anusha'
my_string= 'the person here is %s' % var #says the placeholder here is a string and the value of string
print(my_string)

#in case of digit it is %d and for float it is %f(by default it is 6 digits after decimal point), 
# if two digits are needed then it is %.2f

#formatting using .format()
var1=3.1243456
var2= "tom"
my_string1='the value is {:.2f}'.format(var1) #for 2 digits after decimal
print(my_string1)

#formatting using f-string, evaluation is done using run time
my_string2 = f'the person is {var2} and has a score {var1}'
print(my_string2)

   