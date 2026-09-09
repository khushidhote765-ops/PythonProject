'''
constructor
   it is a function which will be executed by creating the class object then that is called as
   constructor.

   Type of constructor
   a) default constructor
        the constructor which does not have argument then that is called as default constructor.

   b) parametrize  constructor

'''
# class AB:
#     def __init__(self): # default constructor
#         print("hello")
#
# A =AB()




# method overriding: there will be two class with the same function name then that is called as method overloading.

# class AB:
#     def display(self):
#         print("Class AB is call")
#
# class CD(AB):
#     def display(self):
#         print("Class CD is call")
#
# pl = CD()
# pl.display()


class AB:
    def add(self,a,b,c=0):
        print(a+b+c)


z=AB()
z.add(23,56)
z.add(12,9,34)