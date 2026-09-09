'''

a=() # tuple :-> data updation is not allowed. along with duplicate data is also allowed.
a=[] # list : data updation is allowed along with duplicate is also allowed.
a={} # sets : data updation is not allowed. along with duplicate data is not  allowed.
a={:} # dict : its work with key pair values.

'''

a=(12,56,5623,23,5623,35)

print(a)
print(type(a))

b=[45,23,56,12,46,67,23]
print(b)
b[2]="45678"
print(b)

print(type(b))

z={45,23,56,340,56,345,230}
print(z)

print(type(z))

z={'name':'sai',
   'age':33,
   'Location':'pune'}

print(z)
print(z['name'])
print(type(z))