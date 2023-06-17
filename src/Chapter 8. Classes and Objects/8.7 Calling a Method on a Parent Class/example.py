# Problem
"""
You want to invoke a method in a parent class in place of a method that has been overriden in a subclass
"""


# Solution
class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        print("A.__init__")


class B(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        print("B.__init__")


class C(B,A):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        super().__init__()
        print("C.__init__")


if __name__ == "__main__":
    c = C()
    # A method resolution order (MRO) list
    print(C.__mro__)
