#INDENTATION
# print('hello-world')
## indentation is very important(to indicate blocks of codes) also take note of the 'colon'
if 5>3:  
    print('i am bored') 
    print('five is greater than two')

#COMMENT
# Multiline comment
    """
        we are here boss
    """
#singleline comment
    #i am a man
   
#VARIABLES
    x=4 + 2   #output should be an integer
    x='string' #it has now been reassigned to be a string
    print(x)

#CASTING(If you want to specify a data type of a variable)
    t=str(3)
    w=int(4)
    z=float(2)
    print(z)
    print(w)
    print(t)

#GETTING THE DATA TYPE OF A VARIABLE
    x=5
    print(type(x))
    y='the man of the match'
    print(y)

# String variables can be declared making use of single or double quotes
#variable names cannot start with numbers, we cannot make use of hypen also for naming variables, other things that can work for naming variables is the underscore.

    
x,y,z=2,3,4   #python allows you to assign values to multiple variables, number of variables must match the number of values
print(y)
    
t=u=i=4
print(t)
print(i)
print(u)    #python allows you to assign multiple variables to a single value as seen above


#UNPACKING, say
fruits=['apple', 'banana', 'cherry']  #this is a list, as enclosed with  curly braces, just like array in javascript
x,y,z=fruits
print(y)   #banana is the output


#Python allows you to combine text and a variable
the_string='radio'
the_num='45'
print(the_string + " " + the_num)

x=5
y='5'
z=x+int(y)
print(z) #you will get 10, but you cannot add sting and number, you will get error


#PYTHON GLOBAL VARIABLES
#global variables are variables outside of a function, they can be used both inside and outside of a function
#Example:


x='awesome'
def myfunction():
    print('radio')
myfunction()

#we can also have it as
def addtwoThings():
    print(x + ' ' + 'God') #the x that we assiged to a value above can be used in another place and hence x is a global variable
addtwoThings()


#PYTHON DATA TYPES
#we have different data types in python, they are, text type(str), numeric type(int, float, complex), sequence type(list, tuple, range), mapping type(dict), Boolean type(bool)

x=5
print(type(x)) # returns class int


#STRING
x='The advent of AI'
print(type(x)) #returns class string


#FLOAT
y=5.009
print(type(y)) #returns class float

#COMPLEX NUMBER
t=4j
print(type(t))  #this returns class complex


#LIST
w=['john', 'michael', 'vince', 'bruce', 'paul']   #this is a list, curly braces
k=type(w)
print(k)  


#TUPLE
w=('john', 'michael', 'vince', 'bruce', 'paul')  #this is a tuple, brackets



#RANGE
x=range(20)
print(x)


#SET
mySet= {"apple", 'radio', 'mac', 'samsung'}   #this is a set(just like in math where something is enclosed inside of curly braces)
print(type(mySet))


#DICTIONARY(dict) almost similar to objects in Javascript, it also consits of a key and value pair, just like it is in a normal dictionary, a word : and its meaning
myDict={"name":"john", "age":'45', 'height':'34meteres'}
print(type(myDict))

#BOOL
x=False
y=True
print(x)  #returns BOOL 


#SETTING A DATA TYPE BY MAKING USE OF WHAT WE CALL CONSTRUCTORS examples below
string1=str('hello world')   #str is a constructor
print(string1)

int1=int(20)  #int is a constructor
print(int1)

#other constructors that we have are, float, complex, tuple, list, dict, set etc
floatOne=float(30)  # .0 will be added to the output
print(floatOne)



complex2=complex(4)
print(complex2)


#NUMBERS IN PYTHON--numbers consists of FLOAT(decimal and exponentials), INT(whole number, though the real meaning is integer(-ve and +ve)), COMPLEX(complex number)
#converting from one type to another
x=1
y=float(x)
print(y)



w=9.908  
z=int(w)  #it is not going to round up, just going to remove the whole number in front
print(z)
#note that we cannot convert from complex to another type





#RANDOM NUMBERS
#unlike JS, python does not have a random() function, but we can import a random module and make use of it in addition with a function
import random  #after importing this, we can now use it with another function as in random. something
randy=random.random()
print(randy)  # gives a random number(float particulaly) on run

num= random.randint(2,10)   #this will return a random integer between 2 and 10 inclusive
print(num)

#MULTILINE STRINGs IN PYTHON, not we can make use of double or the triple quotes
a= '''we are preparing
     for the final
    match between
    the two team'''
print(a)    #the multiline string will make the output to be the same way and format that it is in a, with the line breaks etc



#just like we have indexes in javascript, same goes for python, now let's see the example below
fruit='banana'
#print(fruit[2])   #this will show what is on index 2 of fruit which is n, do not forget that indexes starts from 0 to anything, so we have 0,1,2,3 etc



#IN PYTHON STRINGS ARE ARRAYS, SO WE CAN LOOP THROUGH A STRING SAME WAY WE CAN LOOP THROUGH AN ARRAY, example
for x in 'banana':
    print(x)    #this is going to loop through banana and ouput the letters in it



#TO GET THE LENGTH OF A STRING, WE USE THE len() FUNCTION, the len() function returns the length of a string
w='oludairo adeteju'
print(len(w))   #16 including the space


t='my name is oludairo adeteju'
print(len(t))

#TO CHECK IF SOMETHING IS CONTAINED IN ANOTHER THING or NOT FOR EXAMPLE(in and not in)
x='only God can bring an end to the conflict between RUssia and Ukraine'
print('Ukraine' in x)  #returns true
print('Ghana' in x) #returns false
print('Nigeria' not in x)   #returns true


#we can apply the checking string in if and else statements
quote='you cannot eat your cake and have it'
if 'you' in quote:
    print('yes, it is contained in there')
else:
    print('it is not contained inside')



countries='russia,lesotho,paraguay,venezuela,bennin,portugal,scotland'
print('scotland' in countries)
print('panama' not in countries)
#we can use the not in and in for an if and else statement




#SLICING STRING IN PYTHON- we specify the start index and the end index, separated by a colon, to return a part of the string
stingy='domicican'
print(stingy[2:3])    #this gives just 'm', 2 is the start index while 3 the 3 index will not be added



#if we leave out the start index
hello='hello world'
print(hello[:5])    # you will get hello as the result, the empty start index means start from the very beginning




hello_two='hello world'
print(hello_two[2:]) #you will get llo world meaning from that place(index 2) to the very end




#NEGATIVE INDEXING- We use negative indexing to start the slice from the end of the screen
my_list=[10,20,30,40,50]
print(my_list[-1])  #this prints out the last item in the list
print(my_list[-4:-2])  #this will start the counting from the back but will not include the very last index(-2) just as it is when dealing with positive integers
print(my_list[-2:])   #this will give 40 and 50
print(my_list[-5:]) #this will give the value from the index of -5 to the last one 


#MODIFYING STRING IN PYTHON
#the upper method return the string in uppeercase
stringy='NBA Youngboy'
print(stringy.upper())  #this is a method like it is in JS
print(stringy.lower())   #this is a method like it is in JS
print(stringy.capitalize())   #this is a method like it is in JS
#we can remove the white space from the end and the beginning of what we were given using the .strip() method

stripping=' there are many meanings to the world radio      '#the space in front and back will be removed
print(stripping.strip())



#we have the replace method
caseone='televison'
print(caseone.replace('t','v'))  #this replaces the t to v so we have velevision

food='coming'
print(food.replace('c', 'f'))




#STRING CONCATENATION
a='hello'
b='world'
c=a+ ' ' + b
print(c)





#STRING FORMAT
age=36
#txt='my name is John, I am' + age
#print(txt)  # you will get error, you cannot add a string and an integer


name='alice'
age=23
print("hello, {}. You are {} years old.". format(name, age)) #. format here means fill up the empty curly braces with name and age respectively 


firstName='Oludairo'
lastName='Adeteju'
MiddleName="Gabriel"
myStatement='{} is my firstname, {} is my lastname and {} is my middlename'
print(myStatement.format(firstName, lastName, MiddleName))   #study the structuring of this


#in string formating, we can make use of index number to be sure that the argument is placed at the correct spot
name='damola'
age=23
profession='tailor'
details='my name is {0}, and i am {1} years old, In addition to this details, i also work as a {2} in a reputable organization'
print(details.format(name, age, profession))



fish='tilapia'
radio='positive fm'
yam='yellow yam'
final='the name of the fish is {}, and the name of the radio station that we heard it is {} afterwards we went to the kitchen to cook {}'
print(final.format(fish,radio,yam))



#ESCAPE CHARACTERS IN PYTHON-they are used to insert illegal characters in a string, we make us of the backslash '\'  for the escape character, 
#for a new line
print("hello\nWorld")

#flashback
def myFUnction(a,b):
    return (a*b)
result=myFUnction(3,5)
#print(result)    


#we use the escape key for tab as in
print('hello\tworld')

#to add two backslashes
print('we are\\\preparing')

#to add a single quote
print('teju\'s phone is an android phone')  #this will make the apostrophe possible without generating an error



text='we are coming from the jungle and we seriously need to eat some food before continuing in our journey'
#print(text.upper())
#print(text.lower())
#print(text.upper())


#PYTHON BOOLEAN
#print(type('rf')==type('fish')) #true
#print(34==34)  #true

a=10
b=3
if(a<b):
    print("i am less")
else:
    print('I am not less')    



#in python, True can be evaluated to 1 while false can be evaluated to be False
calculated=5 + True      
print(calculated)   #you will get 6 as the result


#Evaluation to be true or not, most evaluation is true except for 0 in number and empty string on strings, this is just like the TRUTHY AND THE FALSY IN JS
#print(bool('hello world')) #returns true
#print(bool(34))   #returns true
    
#examples of falsy values are False, None, 0, " ", (). [],{}
    #print(bool(0))
    #print(bool(False))
    #print(bool(()))
    #print(bool([]))   #they are all false



#PYTHON OPERATORS
#we have some python assignment operators e,g, x+=3 means x=x+3, x-=3 means x=x-3, x%=3 means x=x%3 etc


#PYTHON COMPARISM OPERATORS==, !=, >,>=, <=, means equal to, not equal to, greater than or equal to, less than or equal to etc
#PYTHON LOGICAL OPERATOR include and, or,not etc
#PYTHON IDENTITY OPERATOR INCLUDE:is, is not etc
#PYTHON MEMBERSHIP OPERATOR, in and not in



#PYTHON LIST-lists are used to store multiple items in a variable
#to determine the number of items of a list we use the len() function
thislist=['apple', 'pawpaw','cashew','guava']



print(len(thislist))  #it is read as 1 to 4 not in the index manner, list items can be of any data type, i.e the items in the list can be a combination of boolean, string, int etc


#There is a 4 collection data type in python, they are, LIST,TUPLE,SET,DICTIONARY
listy=['apple', 4, False, 'radio','banana']   #we can also check for membership of items in a list
if 'apple' in listy:
    print('yes, apple is in the list')
else:
    print('apple cannot be found in the provided list')


#we can change the item in a list, this is for REPLACING, not INSERTION
thislist=['apple', 'banana', 'cherry', 'orange']
thislist[1]='pawpaw'
print(thislist)


#to change a range of item values, say that we have
thislist=['apple', 'banana', 'cherry', 'orange', 'kiwi','bread','opeyemi']
thislist[1:3]=['fish','rice','beans']
#print(thislist) #if you insert more items than you replace, the new items will be inserted where you specified and the remaining items will move accordingly



#insertion of new items in list-without replacing any other item in the list
this_list3=['apple', 'banana', 'cherry', 'orange', 'kiwi','bread','opeyemi', 'man']
this_list3.insert(3,'frying')  #this means frying should take the fourth index and the other items in from of it should take another index
#print(this_list3)



#one thing we can also do is to append to a list--appending something to a list means you want to add something at the very ending of the list, say that we have-- NOTE THAT APPEND IS A METHOD as in(.append)

my_list=['usa', 'Nigeria','portugal','lebanon','israel','veitnam','peru']
my_list.append('chile')
#print(my_list)  #chile will be  added to the last item on the list

#like we said above, we have the insert method, we just specify the index we want the new item to be inserted in and puut the item
our_list=['rain','sun','weather','winter']
our_list.insert(2,'haze')
print(our_list)


#we can also append a list to another list, by saying for example:
list1=['teju','dolapo','johnson','rita']
list2=['ibikunle','ogolo','ogunjo','adesiji']
list1.extend(list2)
print(list1)


#the extend method does not necessarily have to be a list, we can add a list to a tuple, to a dictionary, etc
listA=['nba','kodak','ross']
listB=('eminem','drdre','icecube')
listA.extend(listB)
print(listA)  #the final result will be a list tho


listA=('nba','kodak','ross')
listB=['eminem','drdre','icecube']
#listA.extend(listB)
#print(listA)   #this will create error, you can only add something to a list, not something to a tuple etc


#we can also remove from a list item, for example
listB=['eminem','drdre','icecube','lil mabu','durk']
listB.remove('durk')
print(listB)
listB.remove('eminem')
listB.remove('lil mabu')
print(listB)


#in Python we have the pop method, the pop method remove the last item from the list, but if we specify the index number, then the item on that index will be removed for example
listB=['eminem','drdre','icecube','lil mabu','durk']
listB.pop(1)
#print(listB)   #3drdre would have been removed from this list




#we can delete an entire list by using the 'del' keyword, note that using a keyword is different from using a method
listB=['eminem','drdre','icecube','lil mabu','durk']
del(listB)
#print(listB), it will tell you that listB is not defined





#there is the .clear() method, it clears the items in the list e.g
listC=['eminem','drdre','icecube','lil mabu','durk']
listC.clear()
#print(listC)  #you will get back an empty list, so the clear method retains the list but just that the items in the list are empty, compared to using the del keyword which wipes away the whole thing called list



#LOOPING
#FOR
#we can loop through a list by using a for loop, say that we have:



forlooping={'eminem','drdre','icecube','lil mabu','durk'}   #whether this is list, dictionary, tuple--they are all iterable
for x in forlooping:
    print(x)  #this will bring out the items in the list, just like the map method in js

teju=range(5) #normally will give us (0,5)
for i in teju: #looping through this will now give us 0,1,2,3,4............ and will be printed  
    print(i)   



thislis=['apple', 'banana', 'cherry']
for x in range(len(thislis)):    #since len gives the length which is 3, range(3) will give us 0,1,2, for will now loop through it to output what is needed
    print(x)
    



#WHILE loop
    #you can loop through a list item by using the while loop, i.e we make use of the while loop to repeatedly execute a block of code as long as  given the condition is true


count=1
while count<=5:   #the loop continues as long as count is less than or equal to 5
    count+=1
    print(count)



#Let us say that we have a list
listy=['teju','damola','paul','kunle']
#[print (i) for i in listy]   #this is a shorthand form of writing a for loop


#LIST COMPREHENSION, you can create an empty list and add from the previous list to that empty list:
#say:

list_of_fruits=['apple','coco','isu','orange','banana','pawpaw','hui','caca']
newlist=[]
for x in list_of_fruits:
    if 'a' in x:
        newlist.append(x)
#print(newlist)

#summary of what i have above is that, we have an existing list, then we have an empty list, we looped through the existing list(x) and then we say if string a 'a' is in anayway included in what we looped through, then append the ones that contain 'a' to the empty list that we created and hence print the newlist tat we are having:

#ITERABLE:
#the iterable can be any iterable object like, list, tuple, set etc
my_list=[x for x in range(0,10)]     #the full meaning is print x for x in range(0,10)
print(my_list)

#another way of wrtiting the above
rangy=range(10)
for i in rangy:
    print(i)

newlist_2=[x for x in range(13) if x<5]   #print for only those less than 5
print(newlist_2)



#another example
fruit=['apple','banana','cherry','kiwi','mango']
newlist=[x.upper() for x in fruit]   #note the order
print(newlist) 
#we had an existing list, then we want to  have a newlist that will loop through the existing list and then make the out uppercase form, take note of THE ABOVE VERY WELL



previous_list=['television','radio','mobile phone','guitar']
new_list3=[x for x in previous_list]  #print x in the uppercase, after looping through the items in the list
new_list=[x.upper() for x in previous_list] 
print(new_list)


new_list3=[x for x in previous_list]  #print x, after looping through the items in the list
print(new_list3)



newlist_4=[x for x in previous_list if 'a' in x]   # note it means print x after looping through previous_list if a is among the letters in the lists, we can also state a condition like [x for x in previous_list if type(x)!='string'] you are free o explore multiple ways of writing it


#PYTHON SORT-python has a sort method that will sort the items in the list alphanumerically for example
this_list=['orange','apple','kiwi','pineapple','banana']
this_list.sort()
print(this_list)    #output will be arranged in aphabetical order



numerical_list=[23,90,12,32,81]   
numerical_list.sort()
print(numerical_list) #it will be arranged in ascending order



numerical_list2=[23,90,12,32,81] 
numerical_list2.reverse() 
#numerical_list2.sort(reverse=True)   #this is going to make sure that the numbers are arranged in descending order, we can use the reverse above or setting reverse to be True while using the sort method
print(numerical_list2)




def myFunction(x):
    return abs(x-50)
print(myFunction(20))    #it returns 30




#the sort method is case sensitive, meaning that it sorts items in the list that starts with CAPITAL letter before the ones with lower case letters for example;
mixture1=['banana','pumpkin', 'Orange','Egusi']
mixture1.sort()
print(mixture1)   #Egusi comes first in the list then Orange before, banana etc





#to perform a case insensitive sort, we use the key,  and say
mixture1=['banana','pumpkin', 'Orange','Egusi']
mixture1.sort(key=str.lower)   #note that .lower does not have ()  attached to it
print(mixture1)




#COPYING A LIST IN PYTHON---by making use of the copy method, say that we have the list
list_one=['ade','bola','opeyemi','bisola','titi']
list_two=list_one.copy()
print(list_two)    #what is inside of list one will be copied into list two or instead of using the copy method, we can just say




list_three=['ade','bola','opeyemi','bisola','titi']
list_four=list(list_three)
print(list_four)  # what we have in list three will be copied into list four and will be printed




#PYTHON JOIN
#joining something in python also means concatenating
listOne=['a','b','c']
listTwo=[1,2,3]
print(listOne + listTwo)   #it will be joined together listOne and listTwo


#we can also make use of the extend method
listOne=['a','b','c']
listTwo=[1,2,3]
listOne.extend(listTwo)
print(listOne)



#we can also make use of the append method but we will need to loop through 
listOne=['a','b','c']
listTwo=[1,2,3]
for x in listTwo:
    listOne.append(x)
print(listOne)    #instead of returning a list inside of a list, listTwo is looped and the items are added individually to list one to form a long list




#PYTHON TUPLES
#a tuple is one of the four in-built data type in python used to store collections of data, the other three are list, set and dictionary


#note that TUPLES in python are immutable-i.e they cannot be changed, we cannot use all these reverse, join method on it
#to create a tuple with one item, we need to add a comma after the first item in the tuple e.g
tupley=('food',)   #this is a tuple if we check the type, we will get <class tuple>
tupley=('food')  #this is a string


#the items in a tuple can be of any type, can be boolean, string, etc
#A LIST IS A COLLECTION THAT IS ORDERED AND CHANGEABLE
#A TUPLE IS A COLLECTION THAT IS ORDERED AND UNCHANGEABLE
#A DICTIONARY IS A COLLECTION THAT IS ORDERED AND CHANGEABLE #meaning only tuple is immutable



#accessing tuple items
thistuple=('rice','beans','yam','egg',5) #we can access the items in this tuple by saying, 
print(thistuple[1])  #just like normal indexing
print(thistuple[-1]) # means print the last one
print(thistuple[2:4])  #just like normal slicing


#we can check if an item is in a tuple by saying
tupleme=('we are preparing for a long jorney that will shape our life')
if 'are' in tupleme:
    print('okay you are welcome')
else:
    print('you are not in any way welcome here')

#we can quickly convert a tuple to a list by saying
top=('fish','radio')
bottom=list(top)
print(bottom)  #it will completely become a list with the result ['fish','radio'], and we can do what can be done to a list with it, i.e you can append to it e.t.c. convert the tuple to a list, add your item, and convert it back to a tuple


#on a side note you can concatenate two lists in python, instead of using append and all those stuffs
listme=['ope','titi','bola','ayo','labake','johnny','kiki']
listmy=['ope','titi','bola','ayo','labake','johnny','kiki']
listr=listme+listmy
print(listr)



#you are allowed to add a tuple to a tuple in python
tuple1=('we','are','dancing')
tuple2=('they','aree','joing')
tuple3=tuple1+tuple2
print(tuple3), #tuple1 will continue along with tuple 2



#you cannot use the remove method on tuples, but you can use the del function to delete the entire tuple itself
#tuples are immutable; i.e the values inside cannot be changed but just like the above, we can convert it to a list first, do any changes we want to do and then convert back to a tuple. 

my_tuple=('our','father','who','art')
conve=list(my_tuple)
conve.append('in heaven')
print(conve)
final=tuple(conve)
print(final)  #we are finally converting the result back to a tuple



#UNPACKING TUPLES
#we can unpack tuples by saying, 
foods=('fufu','rice','beans')
(first, second, third)=foods
print(first)
print(second)
print(third)   #values on the left hand side will be attached to the values on the right hand side. just like saying we are assigning variables to values



#using asterisks----it used if the number of variables is less than the number of values for example
fruits=('pawpaw','orange','banana','mango','cashew','grape','guava')
(red, blue, *green)=fruits
print(green)    # this will take banana, mango, cashew, grape and guava
print(red) #this will print out pawpaw


#looping through tuples
thistuple=('apple','mango','peeper','drama','ginger')
for x in thistuple:
    print(x.upper())   #loop through the tuple and print out individual items in the tuple in capital letter


#joining tuples
tupl1=('a','b','c')
tupl2=('d','e','f')
print(tupl1+tupl2)   #you can concatenate tuples.


#we can also multiply tuples
#for example
thistuple=('apple','mango','peeper','drama','ginger')
print(thistuple*2)





#PYTHON SETS, just like the tuple, list, set is used to store multiple items in a single variable, it is one of the four built in data type in python


thisset={'apple', 'orange','mango','pineapple'}, #they are written with curly braces
#in a set duplicate values are not allowed, i.e we cannot have 'apple' twice in the list
thisset={'apple', 'orange','mango','pineapple','apple'}
print(thisset)  #only one apple will come out
#items in a set can be boolean, strings, integers etc
#if we want to make a set, we can use the set constructor, by saying set()
ourset=set(('appple','rice','orange','noodles'))  #note the double braces, not even curly braces



#accessing items in a set, we cannot access items in a set by using index number or a key, but we can loop through the set by using the for loop
mySet={'food','bag','money','radio', 'fish'}
for x in mySet:
    print(x.upper())
print('food' in mySet)   #this will give out True
#ONCE a set is created, you canot change the items but you can add new items to it, by using the add() method


set1={'von','kodak','juice','youngboy'}
set1.add('quavo')
print(set1)


#we can add iterables to a set, i.e we can add tuples, dictionary or lists to a set by using the update() method
setA={'apple','banana','cherry'}
setB={'1','2','3'}
setA.update(setB)
print(setA)   #what is inside of set B will be added to that of set A



#To remove set items
#to remove an item in a set, we use the remove method, let us say tha we have a set
thisset={'apple','banana','oranges','pawpaw'}
thisset.remove('apple')
print(thisset)



#if the item you want to remove in a set does not exist, it will throw an error, but instead of using remove in this scenario, we can make use of the discard method,
thisset.discard('pawpaw')
print(thisset)



#we can also remove the last item in a set by using the pop method; 
thisset={'apple','banana','oranges','pawpaw'}
thisset.pop()
print(thisset)   #anyone of the items in the listis removed, remember that the items in a set are unordered, so anyone of them can be removed
#we can also use the  clear method to empty a set,
thisset={'apple','banana','oranges','pawpaw', 'grape'}
thisset.clear()
print(thisset)  #this is going to give u an empty set, but the set will still exist, we use the del keyword to delete the set completely just like we have in tuple


thisset={'apple','banana','oranges','pawpaw', 'grape'}
del(thisset)
#print(thisset)   #you will get anerror that says thisset is not defined



#we can loop or iterate set items
thissety={'apple','banana','oranges','pawpaw', 'grape'}
for x in thissety:
    print(x)   #item in the set will be listed out



#we also can make use of the update and union to add sets to sets
#the update method updates the existing set, while the union method creates a nnew set which contains the items in th efirst set and the items in the second set #for example;
    
set1={'a','b','c','d'}
set2={'e','f','g','h'}
set1.update(set2)  #set1 will retain it items while adding the items in set 2, do not forget that the items in a set are unordered, meaning that the canbe arranged in any form, no particular form of arrangement
print(set1)


#union
set1={'a','b','c','d'}
set2={'e','f','g','h'}
set3=set1.union(set2)  # you need to create a new set to be able to use the union method, like a union in Mathematics {SET}
print(set3)




#DICTIONARIES IN PYTHON, it is a like a key value pair, but this key value pairs are both strings
#a dictionary is a collection which is ordered, changeable, and does not allow duplicates
    
thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
print(thisdict["brand"]) #study the syntax very well, this will print out 'ford' as the answer

#a dictionary cannot have the same item with the same key; so we say that in a dictionary, duplicates are not allowed

thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
print(len(thisdict))   #gives 3 i.e three items in the list


#dictionary is just like an object in javascript, it can take any data type for example;
thisdict={
    "brand":'ford',
    "electric":"false",
    "colors":["red","blue","green","yellow"] #meaning that you can have a list as the value of a key
}
#we can check for the type of the dictionary and we get <class 'dict'>
#we can access the items in a dictionary by using the key name

thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
print(thisdict['brand'])  #it will print out ford

#we can also use a method called .get, it will bring out the same result as using the curly braces
#let us say that we have
x=thisdict.get("model")
print(x)   #it will print out mustang


#there is the .key method, this returns the lists of the keys in the dictionary;
thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
print(thisdict.keys())



#we can add a new item to an object by saying
thisdict['price']='$3000'
print(thisdict)



#same way that got the keys, we can also get the values, by saying
print(thisdict.values()) #just the values in the object will be printed

thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
print(thisdict.items)


if "model" in thisdict:
    print('yes, model is among the keys')
else:
    print('no, i do not know nothing')



thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}

thisdict['year']='1992'  #change the year from 1964 to 1992
print(thisdict)



#removing items in a dictionary
thisdict={
"brand":"ford",
"model":"Mustang",
"year":"1964"
}
#we can make use of the pop method, 
thisdict.pop('brand')
print(thisdict)

#if we use the popitem, it removes a random item from the list,
thisdict.popitem()
print(thisdict)

#the del keyword removes the item with the specified key name:
thisdict1={
    'name':'oludairo',
    'age':'34',
    'height':'34meters'
}

del thisdict1['age']
print(thisdict1)



#we can also use the clear() method to empty the dictionary
thisdict1={
    'name':'oludairo',
    'age':'34',
    'height':'34meters',
    'fiancee':'none'
}
thisdict1.clear()
print(thisdict1)   #you will get an empty dictionary




#looping through a dictionary
#you can loop through a dictionary using the for loop, 
thisdict1={
    'name':'oludairo',
    'age':'34',
    'height':'34meters',
    'fiancee':'none'
}
for x in thisdict1:
    print(x)   #it will return the keys


#to get the values,we say
for x in thisdict1.values():
    print(x)
#we also have
for x in thisdict1.keys():
    print(x)
#we can also have the command, 
for x,y in thisdict1.items():
    print(x,y)



#copying a dictionary
originaldict={
    "name":"teju",
    "age":'32',
    'height':'34'
}
duplicatedict=originaldict.copy()
print(duplicatedict)  #what is in the originaldict will be copied to the duplicate one, we canmake a copy by saying
originaldict={
    "name":"teju",
    "age":'32',
    'height':'34'
}

duplicatetwo=dict(originaldict)  #does the same work as the .copy method
print(duplicatetwo)

#nested dictionaries
child1={
    "name":"Emilly",
    "year":2004,
    "courses":{
        "phy":{
            "phy203":'32',
            "phy204":'32',
            "gns304":"34"
        },
        "mth":'79',
        "csp":'82',
        "ent":"90"
    },
    'fame': False
}
print(child1)


#this is me trying to write a nested dictionary in python off the top

mynesteddict={
    "firstly":"omo",
    "secondly":{
        "nested":'1',
        'nested2':'2',
        "nested3":"3"
    }
}



#PYTHON IF AND ELSE STATEMENT
a=3
b=4
if a>b:
    print('i am greater')
else:
    print('i am not greater')

c=4
d=3
if c!=d:
    print('okay')
else:
    print('i do not know')



#elif-elif in python is a way of sayin, if the previous condition is not true, then try this condition
a=34
b=35
if a>b:
    print('okay it is truly greater')
elif(a<b):
    print('okay, we are cool now')
else:
    print("i can't say anything about this")


#SHORTHAND IF:
e=12
f=34
print('e is greater') if e>f else print('e is not greater')  #note that there is no colon in front of if and else, this expression is ternary operator or conditional expression

#AND, it is a logical keyword and it is used to combine conditional statements
a=200
b=300
if a and b > 100:
    print('truly they are greater than 100')
a=200
b=300
c=350
if a>b and b>c:
    print('it is logical')
else:
    print('it is complicated')
#OR, it is also a logical keyword and it is used to combine conditional statements
a=200
b=240
c=333
if a or b>100:
    print('for sure, it is greater')
else:
    print('I do not know')




#we have the pass keyword; if the if statement has no content, then we can use the pass statement to avoid getting an error
a=33
b=200
if b>a:
    pass

i=1
while i<6:
    print(i)
    i+=1
#we can make use of the continue and breakk keywords in python also, refer to materials for examples;
    
#FOR LOOP
#with the for loop, we can iterate over a sequence(that is a list, or tuple or dict, a set, a string etc)



#we have the break statement; with the break statement, we can stop the loop at a particular point before it loops through all the items in the sequence
fruit=['apple','mango','pineapple']
for x in fruit:  #do the iteration
    if x=='mango':
        break
    #print(x)   #only apple will be in the output;

#apart from the break keyword, we also have the continue keyword whose function is to basically stop at a particular declaration and continue with the next operation for example:


fruity=['apple','mango','pineapple','pawpaw','vine'] 
for i in fruity:
    if i=='banana':   #it means omi banana and move on to the next item on the list
        continue
    print(i)
 
 #the range function
for x in range(6):  #default starting point is 0
    print(x)

#for x in range(0,6):   #loop through, start from 0 and stop at 5, 6 is not included
    #print(x)

for x in range(2,6):  #loop through, start from 2 and stop at 5, 6 is not included
    print(x)


#we can add a third parameter to the range which is known as the increment or the step for example;
for x in range(2,30,4):
    print(x)   #start from 2, add 4 add 4 again but never include 30


for x in range(6):
    print(x)
else:
    print('finally finished') #it means the code(print finally) will not run unless the  range is command is completed

#nested loop-a nested loop is a loop inside of a loop, the nested loop will be executed one time for each iterationof the outer loop
    #example of a nested loop
adj=['red','big','tasty','small','tall','bright']
verb=['come','play','dance','fight','jump']
for x in adj:
    for y in verb:
        print(x,y)  #red come, red play, red dance ............. does same for big, does same for tasty etc


#FUNCTIONS in python--a function is a block of code which only runns when it is called
        
def myfunction(a,b):
    print(a+b)  #a and b are the arguments/parameter
        
myfunction(2,3)

#by default in python a function must be called with the correct number of arguments, meaning that if your function expects two arguments, you have to call  the function with the two arguments


#this is a way of sending arguments with the key value syntax
def myFunctiont(child1, child2, child3):
    print('my first kid is' + ' '+ child3)
myFunctiont(child1='Damola', child2='Teju', child3='Ope')  #it is just like normal way of passing an arguments into a function just that we are using key value syntax


#we have the default parameter, which means, if we call the function without the parameter, the default argument that we passed in will be used
def myDefaultfunction(country="Azerbaijan"):
    print('my default value otherwise chnaged is' + " "+ country.capitalize())
myDefaultfunction('rwanda')  #rwanda will bw used for the position of country
myDefaultfunction() #the default parameter will be used
myDefaultfunction(country='Lesotho')  #the default parameter will be replaced with Lesotho



#here we are passing a list as an argument; we can send any data type into the argument, be it list, or dictionaries etc
def funcky(food):
    for x in food:
        print(x)
fruits=['apple','orange','banana','cashew']
funcky(fruits)




#next thing that we have is the return values-to let a function return a value, use the return statement/keyword
def function1(c):
    return(c*5)
result=function1(5)
print(result)



#functions cannot be empty, but for any reason we will be needing an empty function, then we can use the pass statement inorder to avoid error
def ourFunction():
    pass



#PYTHON LAMBDA-a lamda function is a small anonymous function, it can take any number of arguments but can only have one expression
#syntax-lamda arguments:expression, the expression is executed and the result is returned
x=lambda a: a +10
print(x(5))

y=lambda t,r: r+t+15
print(y(3,4)) #two things are expected as the parameters


c=lambda a: a*10   #you can add as many parametrs as you want in the argumets side
print(c(10)) 


#to multiply three 3 digits
w= lambda x,y,z: x*y*z
print(w(2,3,4))



#PYTHON ARRAYS--there is array proper that can be imported from libararies in python but for now we are making use of the list
#ARRAYS are used to store multiple values in one single variable
#we can refer to an element in an array by referring to the index number:
cars=['ford','mustang','g-wagon','porsche']
#print(cars[1])
cars[2]='radio'
print(cars)





    





      


    





    
    





























































