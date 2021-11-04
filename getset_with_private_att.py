"""

Usage of getters and setters in python:

1) add validation logic around getting and setting a value.

2) To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

"""


class Geek:

    # one way of implementation is using private attribute with "__"

    def __init__(self, a=0):
        self.__age = a

    # getter method
    def get_age(self):
        print("Getter method called")
        return self.__age

    # setter method
    def set_age(self, x):
        print("Setter method called")
        self.__age = x

    def del_age(self):
        print("DEL method called")
        del self.__age

    # _age = property(get_age, set_age, del_age)


pet = Geek()
print("=" * 25)
print(pet.get_age())
pet.set_age(21)
print(pet.get_age())
print("=" * 25)

