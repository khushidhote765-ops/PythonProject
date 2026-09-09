'''
h) Loop
 it is used to repeat the block of a code or a statement then that is called as
 loop.

   a) while loop
      it is a entry control loop.

   b) for loop
      it is a entry condtrol loop

a=1
while a<=10:
    print(a)
    a=a+3



for i in range(1,11):
    print(i)

'''

n=int(input())
a=1
while a<=100:
    print("%d * %d = %d "%(n,a,a*n))
    a=a+4