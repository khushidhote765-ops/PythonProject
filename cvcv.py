# # single inheritance
# class A:
#     def display(self):
#         print("Hello class A")
#
#
# class B(A):
#     def dis(self):
#         print("Hello class B")
#
#
# b =B()
# b.dis()
# b.display()

# multilevel inheritance
# class A:
#     def display(self):
#         print("A")
#
#
# class B(A):
#     def displayB(self):
#         print("B")
#
#
# class C(B):
#     def displayC(self):
#         print("C")
#
#
# c= C()
# c.display()
# c.displayB()
# c.displayC()


# multiple inheritance
class A:
    def display(self):
        print("A")


class B:
    def displayB(self):
        print("B")


class C(A,B):
    def displayC(self):
        print("C")


c= C()
c.display()
c.displayB()
c.displayC()