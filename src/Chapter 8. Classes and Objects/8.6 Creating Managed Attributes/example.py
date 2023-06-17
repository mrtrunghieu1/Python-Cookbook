# Problem
"""
You want to add extra processing (eg., type checking or validation) to the setting of an instance attribute.
"""


# Solution

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


if __name__ == "__main__":
    person_a = Person("Hieu Vu")
    print(person_a.first_name)
