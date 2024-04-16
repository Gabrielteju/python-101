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
#variable names cannot start with numbers, we cannot make use of hypen also nameing variables, other things that can work for naming variables is the underscore.

    
x,y,z=2,3,4   #python allows you to assign values to multiple variables, number of variables must match the number of values
print(y)
    
t=u=i=4
print(t)
print(i)
print(u)    #python allows you to assign multiple variables to a single value as seen above


#UNPACKING, say
fruits=['apple', 'banana', 'cherry']  #this is a list, as enclosed with a burly braces, just like array in javascript
x,y,z=fruits
print(y)

#Python allows you to combine text and a variable
the_string='radio'
the_num='45'
print(the_string + " " + the_num)

x=5
y='5'
z=x+int(y)
print(z) #you will get 10, but you ccanno add sting and number, you will get error


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
w=['john', 'michael', 'vince', 'bruce', 'paul']  #this is a list, curly braces
k=type(w)
print(k)  


#TUPLE
w=('john', 'michael', 'vince', 'bruce', 'paul')  #this is a tuple, brackets

#RANGE
x=range(20)
print(x)


#SET
mySet={"apple", 'radio', 'mac', 'samsung'}   #this is a set
print(type(mySet))


#DICTIONARY(dict) almost similar to objects in Javascript, it also consits of a key and value pair,
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

num= random.randint(2,10)   # this will return a random integer between 2 and 10 inclusive
print(num)

#MULTILINE STRINGs IN PYTHON, not we can make use of the double of the double or the triple quotes
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


# TO GET THE LENGTH OF A STRING, WE USE THE len() FUNCTION, the len() function returns the length of a string
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
print(my_list[-4:-2])  #this will start the counting fromt ehback but will not include the very last index(-2) just as it is when dealing with positive integers
print(my_list[-2:])   #this will give 40 and 50
print(my_list[-5:]) #this will give the value from the index of -5 to the last one 


#MODIFYING STRING IN PYTHON
#the upper method return the string in uppeercase
stringy='NBA Youngboy'
print(stringy.upper())  #this is a method like it is in JS
print(stringy.lower())   #this is a method like it is in JS
print(stringy.capitalize())   #this is a method like it is in JS
#we can remove the white space from the end and the beginning of what we were given using the .strip() method

stripping=' there are many meanings to the world radio     '   #the space in front and back will be removed
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
#print(age)  # you will get error, you cannot add a string and an integer


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


#Evaluation to be true or not, most evaluation is true except for 0 in number and empty string on strings, this is just liek the TRUTHY AND FALSY IN JS
#print(bool('hello world')) #returns true
#print(bool(34))   #returns true
    
#examples of falsy values are False, None, 0, " ", (). [],{}
    #print(bool(0))
    #print(bool(False))
    #print(bool(()))
    #print(bool([]))   #they are all false

#PYTHON OPERATORS
#we have some python assignment operators e,g, x=+3 means x=x+3, x-=3 means x=x-3, x%=3 means x=x%3 etc

#PYTHON COMPARISM OPERATORS==, !=, >,>=, <=, means equal to, not equal to, greater than or equal to, less than or equal to etc
#PYTHON LOGICAL OPERATOR include and, or,not etc
#PYTHON IDENTITY OPERATOR INCLUDE:is, is not etc
#PYTHON MEMBERSHIP OPERATOR, in and not in


#PYTHON LIST-lists are used to store multiple items in a variable
#to determine the number of items of a list we use the len() function
thislist=['apple', 'pawpaw','cashew','guava']

print(len(thislist))  #it is read as 1 to 4 not in the index manner, list items can be of any data type, i.e the items in the list can be a combination of boolean, string, int etc
#There a 4 collection data type in python, they are, LIST,TUPLE,SET,DICTIONARY
listy=['apple', 4, False, 'radio','banana']   #we can also check for membership of items in a list
if 'apple' in listy:
    print('yes, apple is in the list')
else:
    print('apple cannot be founf in the provided list')

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
this_list3.insert(3,'frying')
#print(this_list3)


#we can also append to a list--appending something to a list means you want to add something at the very ending of the list, say that we have-- NOTE THAT APPEND IS A METHOD as in(.append)

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

#the extend methid does not necessarily have to be a list, we can add a list to a tuple, to a dictionary, etc
listA=['nba','kodak','ross']
listB=('eminem','drdre','icecube')
listA.extend(listB)
print(listA)  #the final result will be a list tho


listA=('nba','kodak','ross')
listB=['eminem','drdre','icecube']
#listA.extend(listB)
#print(listA)   #this will create error, you can only add something to a list, not something to a tuple etc


#we can also remove from a lsit item, for example
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
#print(listC)  #you will get back an empty list

#LOOPING
#FOR
#we can loop through a list by using a for loop, say that we have:

forlooping={'eminem','drdre','icecube','lil mabu','durk'}   #whether this is list, dictionary, tuple--they are all iterable
for x in forlooping:
    print(x)  #this will bring out the items in the list, just like the map method in js


#WHILE loop
    #you can loop through a list item by using the while loop, 




















