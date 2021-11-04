# Implementing setters and getters using @propery decorator
class Employee:

    def __init__(self, name, company):
        self._name = name
        self.__company = company  # __ denotes as a private attribute

    @property
    def company(self):
        print("@property class method called")
        return self.__company

    @company.setter
    def company(self, value):
        print("@company.setter class method called")
        self.__company = value


e = Employee('Pranay', 'Amazon')
print("Company name is :", e.company)
print("=" * 35)
e.company = 'Google'
print("Company name is :", e.company)
print("=" * 35)
Employee.company = 'Microsoft'  # set the value by calling the propery method using class name
print("Company name is :", Employee.company)