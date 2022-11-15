# 1. Write a Rectangle class allowing you to build a rectangle with length and width attributes.
# 2. Create perimeter() and area() methods to calculate perimeter and area of rectangle
# 3. Create a display() method that displays length, width, perimeter, and area of an object
    # using an instantiation on rectangle class.
# 4. Create a Parallelepiped child class inheriting from the Rectangle class w/ a height attribute
    # and another volume() method to calculate volume of parallelepiped
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width
    def display(self):
        print(self.length, self.width, self.perimeter(), self.area())

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        print(self.area() * self.height)

rectangle1 = Rectangle(10, 5)
rectangle1.display()
parallelepiped1 = Parallelepiped(10, 5, 5)
parallelepiped1.volume()

# 1. Create class Person with attributes name & age of type str
# 2. Create display() method to display name & age of object created via Person class
# 3. Create child class Student which inherits from Person class and also has section attribute
# 4. Create method display_student() that displays name, age, section of object
# 5. Create student object via instantiation on student class and then test display_student()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)
    def display(self):
        for info in vars(self).values():
            print(info)

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
    def display_student(self):
        for info in vars(self).values():
            print(info)

John = Person("John", 30)
John.display()
Mary = Student("Mary", 12, "B")
Mary.display_student()

# 1. Create class called Bank Account with attributes account_number (int), name (str), balance.
# 2. Create constructor with parameters account_number, name, balance
# 3. Create deposit() method which manages deposit actions
# 4. Create withdrawal() method which manages withdrawal actions
# 5. Create bank_fees() method to apply fees w/ percentage of 5% of balance
# 6. Create display() method to display all account details
class Bank_Account:
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = str(name)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self
    def bank_fees(self):
        self.balance *= .95
        return self
    def display(self):
        for info in vars(self).values():
            print(info)
        return self
user_account1 = Bank_Account(1, "primary", 1200)
user_account1.deposit(100).display().withdrawal(50).display().withdrawal(4000).bank_fees().display()

# 1. Definie a Circle class allowing to create a circleC (O,r) with center O(a,b) and radius r
# 2. Define an area() method to calculate area of the circle
# 3. Define circumference() method to calculate circumference
# 4. Define test_belongs() method of class which allows to test whether point A(x,y) belongs to the
    # circleC (O,r) or not
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def area(self):
        3.14 * (self.r ** 2)
        return self
    def circumference(self):
        2(3.14 * self.r)
        return self
    # def test_belongs(self):
    #     # unsure what this is asking

# 1. Create computation class w/ default constructure allowing it to perform various calcs on ints
# 2. Create factorial() method to calculate factorial of int
# 3. Create method called sum() to calculate sum of first n ints
import math
class Computation:
    def __init__(self):
        pass
    def factorial(self, num):
        return (math.factorial(num))
    def sum(self, n):
        

comp1 = Computation()
print(comp1.factorial(3))
