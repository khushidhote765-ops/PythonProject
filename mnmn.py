'''
Function
  it is a block of a statement or code which is used to perform
  specific task then that is called as functions.

  Type of function
  a) function with  no argument and no return type.
  b) function with argument and no return type.
  c) function with no argument and return type.
  d) function with argument and return type.


a) function defined
      where we are suppose to create the business logic.

b function call
      it help us to execute the function defined.





#  a) function with  no argument and no return type.
def addition(): # function defined
    a=13
    b=90
    print("addition=",(a+b))



def substraction():
    a=9
    b=44
    print("substraction=",(a-b))


addition() # function call
addition() # function call
addition() # function call
substraction()




* Argument
   when we pass the value or declare the variable into the
   parenthises then that is called as argument.

#  b) function with   argument and no return type.
def addition(a,b): # function defined
    print("addition=",(a+b))




addition(45,2) # function call
addition(12,8) # function call



* Return
   it is used to return the value from when it is been executed.


#  d) function with   argument and   return type.
def addition(a,b): # function defined
    return a+b




print("Addition=",addition(45,2) )# function call
print("Addition=",addition(12,8)) # function call



#  c) function with no  argument and   return type.
def addition(): # function defined
    return 12+45




print("Addition=",addition() )# function call
print("Addition=",addition()) # function call

'''

#  c) function with no  argument and   return type.
def addition(): # function defined
    return 12+46




print("Addition=",addition() )# function call
print("Addition=",addition()) # function call
print("addition=",addition())