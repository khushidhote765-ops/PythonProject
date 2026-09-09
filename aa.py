'''

a=() # tuple :-> data updation is not allowed. along with duplicate data is also allowed.
a=[] # list : data updation is allowed along with duplicate is also allowed.
a={} # sets : data updation is not allowed. along with duplicate data is not  allowed.
a={:} # dict : its work with key pair values.

'''

a=(12,56,35,4567,5623,35)

print(a)
print(type(a))

b=[12,56,23,5623,455,35,35]
print(b)
b[2]="4567 "
print(b)

print(type(b))

z={45,45,23,56,12,56,230}
print(z)

print(type(z))

z={'name':'om',
   'age':35,
   'location':'nagpur'}

print(z)
print(z['name'])
print(type(z))

