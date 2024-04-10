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
fruits=['apple', 'banana', 'cherry']  #this is a list, as enclosed with a burly braces
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


#DICTIONARY(dict) almost similar to objects in Javascript, it also consits of a key and value pair that we work with
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