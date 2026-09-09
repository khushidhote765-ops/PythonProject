'''

if else
  in this when the if condition will be true it will execute the
  if body and when the if condition will be false it will execute the else body.

a=12
b=90

if a==b:
    print("Hello")
else:
    print("World")


a=int(input())
b=int(input())
c=int(input())
if a==b:
    print("Hello")
else:
    print("World")


b) elif
   it is used to check multiple condition and in this
   which ever condition will be true it will execute
   that condition body and will not check another condition
   whether it is true or false.


a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a==b:
    print("Hello")
elif a>b:
    print("World")
elif a<=c:
    print("World1")
elif c>=b:
    print("World2")
else:
    print("World3")



c) nested if else
   when we put condition into another condition
   then that is called as nested if else.


'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a==b:
    if c<=d:
        print("Hello")
    else:
        print("World1")
else:
    print("World3")
