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
txt='my name is John, I am' + age
#print(age)  # you will get error, you cannot add a string and an integer













