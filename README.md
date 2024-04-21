# OOP
# The problem
# Method 1 (without using OOP)
# 1st item
item_name = "Phone"
item_price = 100
item_quantity = 3

# # 2nd item
item_name = "Laptop"
item_price = 1000
item_quantity = 2


# Here you have noticed that we are defining the attributes of an entity which is starting from the same prefix
# Here if we print the data types of each attribute we have defined above we will get their data types in terms of class
#  such as <class 'str'>
# here we have notice that every data type is an instance of a class. In the same way we can create our own data types using classes
# Here we can use something like classes

# method 2 (using OOP)

class Item:
    pass

# Here we are gonna instanciate the class. Instance and class both are same


myitem = Item()
myitem.name = "phone"
myitem.price = 100
myitem.quantity = 3

myitem2 = Item()
myitem2.name = "laptop"
myitem2.price = 1000
myitem2.quantity = 1


print(myitem.name)
print(myitem2.name)

# here output would be
# phone
# laptop

# Here you have noticed that we are hard coding our attributes like myItem.name etc. There is a better way of doing this
# This can be done by using specail methods
# Method 3:


class Item:
    def __init__(self):
        print("I am created")

# # here when ever I will create an instance of my class Item. init method would be called and "I am created will be printed".
# # This will be printed as many times as I will create the instance of my class. So we can take benefit of it. That I will explain
# # later. Here "self" parameter is the class itself. Which python pass by default as an argument.


myitem = Item()
myitem.name = "phone"
myitem.price = 100
myitem.quantity = 3

myitem2 = Item()
myitem2.name = "laptop"
myitem2.price = 1000
myitem2.quantity = 1


print(myitem.name)
print(myitem2.name)

# Taking benefit of init method


class Item:
    def __init__(self, name, price, quantity=0):
        # here we are assigning the attributes to some keywords
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

# # here quantity=0 is showing a default value of 0 in case of no item has been purchased.


myitem = Item("Phone", 100, 3)
myitem.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.calculateTotalPrice()
# # what if there is a specific property which is related to a specific obejct for example some laptops have separate num pad and
# # some dont have so in such case we can do something like

myitem2.numPad = False

print(myitem.name)
print(myitem2.name)
print(myitem2.numPad)

# *************************Defining types of the arguments that we are receiving
class Item:
# here we have defined our types of the receiving arguments
    def __init__(self, name: str, price: float, quantity=0):

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")


myitem1 = Item("Phone", 100, 3)
myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.calculateTotalPrice()


myitem2.numPad = False


print(myitem.name)
print(myitem2.name)
print(myitem2.numPad)


# here we have defined our types of the receiving arguments

#*************Assertions
//Assertions in python are used to validate the incoming data into the classes. It takes two arguments. One is the logic
//for validation and other is the message on failing the validation
class Item:
    def __init__(self, name: str, price: float, quantity=0):

        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty

        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")


myitem1 = Item("Phone", 100, 3)
myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.calculateTotalPrice()


myitem2.numPad = False


print(myitem1.name)
print(myitem2.name)
print(myitem2.numPad)

#*******************Class attributes vs Instance attributes
Class attributes:
In simple words Class attributes are the attributes that can be access without creating the instance of the class.
To create such class attributes we have to define them before ini method.

Instance attributes:
All attributes that are inside the init method are called instance attributes. These attributes cannot be access without creating
the instance of their class. The instance must have to create first before accessing their attributes

**NOTE**: We can also create class attributes only for specific instance. Later I'll show you the example

class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * Item.pay_rate #here we are again directly pointing to the object Item


myitem1 = Item("Phone", 100, 3)
myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.calculateTotalPrice()
myitem2.numPad = False


print(Item.pay_rate) 
#here we have directly gave the reference to the object and got access to the pay_rate without creating the instance

print(myitem1.pay_rate)
print(myitem2.pay_rate)

print(myitem1.applyDiscount())
print(myitem2.applyDiscount())

#here above "print(myitem1.pay_rate) print(myitem2.pay_rate)" you might be noticing that for instance myitem1 and myitem2 how 
#we are able to access the pay_rate attribute which is not defined inside init method?

#The reason is that we are able to access the class attribute inside instance is that python always first look for the attribute
#inside the init method if it is not there then it will look inside the class attribute.

******************Using a different value of class attribute for specific instance
What if there is a case that for laptops we want to give the discount of 30% so for that case our value 
of pay_rate should be should be 0.7. But we cannot hard code or change it by directly going into the class attributes. Actually
we need two different values. 0.8 for the phone and 0.7 for the laptop. This is how you can do that:


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate #<---now for pay_rate you have to use self keyword instead of ref to Item class


myitem1 = Item("Phone", 100, 3)
myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.pay_rate = 0.7 # <---------this is how you will do that
myitem2.numPad = False
myitem2.calculateTotalPrice()


print(Item.pay_rate)
print(Item.pay_rate)
print(myitem1.pay_rate)
print(myitem2.pay_rate)
print(myitem1.applyDiscount())
print(myitem2.applyDiscount())

#****************__dict__ method
This is a special method which is Actually used to convert the data into dictionary.
We can use this method on our classes and their instances to see their instances and attributes respectively in the 
dictionary format

class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

myitem1 = Item("Phone", 100, 3)
myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.pay_rate = 0.7
myitem2.calculateTotalPrice()
myitem2.numPad = False


# print(Item.__dict__)
# print(myitem1.__dict__)
# print(myitem2.__dict__)

print(Item.all)

#we can also do something like below using loops to print the name of instance line by line
for instance in Item.all:
    print(instance.name)


#*****************__repr__
This method is used to have a good representation of all the instances of your class.
If you would have so many instances. Then this would be easier to track them by using repr special method
it stands for representation. This method would be call automatically if we are trying to print instances using iterative approach

class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


myitem1 = Item("Phone", 100, 3)
# myitem1.calculateTotalPrice()


myitem2 = Item("Laptop", 1000, 2)
myitem2.pay_rate = 0.7
# myitem2.calculateTotalPrice()
myitem2.numPad = False


print(Item.all)
print(myitem1)


#output
[Item('Phone',100, 3), Item('Laptop',1000, 2)]
Item('Phone',100, 3)


*************Difference between __str__ and __repr__ Method

__repr__: This method is used to return a string representation of the object, which should be as unambiguous
(expressed in a way that makes it completely clear what is meant) as possible. It is primarily used for debugging and 
development. If you call repr() on an object, Python returns the result of this method. 
If __str__ is not defined, __repr__ is used as a fallback. It is a good practice to define the string inside the __repr__
function as it is defined while creating instance e.g f"Example({self.x}, {self.y})"

__str__: This method is used to return a string representation of the object, which should be readable and understandable to 
the end-user. It's intended for display purposes. If __str__ is defined, it is called when the built-in str() function or print() 
function is invoked on the object.

class Example:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Example({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

obj = Example(3, 4)
print(obj)  # Calls __str__, prints: (3, 4)
print(str(obj))  # Calls __str__, prints: (3, 4)
print(repr(obj))  # Calls __repr__, prints: Example(3, 4)

//***********************Class Methods vs static method
Class methods and static methods are the user defined methods that are defined by using decorators such as @classmethod and @staticmethod respectively. The main difference between class and static method is that class method takes the class reference itself as the first argument automatically in the background. Whereas static method is do not take the class as the first argument but a regular argument.

Both methods can also be called directly from the class without creating an instance. They can also be called by creating instance. But that does not make sense to use class or static method to be called on an instance. What was the point of making an instance you can simply use regular function for that purpose.

Below we will use class and static method:

import csv


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.is_integer(7.6))
print(Item.all)


****************When to use Class method and when to use Static method:
Use static method when the method must have some relation with the class but not something that is unique per instance. Like our is_integer method. Which have some relation with the class but do not have unique relation per instance.

Use Class method when you also have some relation with the class but you want to manipulate the structure of data to instantiate the class. like we did with instantiate_from_csv()



****************Inheritance 
Inheritance is one of the most powerful concept in OOP that solves a very big problem. To understand inheritance lets understand a scenario.
Let say you as you have created Item class above. In which we can also have an instance of phone. As phone is also an item. So, let say you want to create a function that tells you that how many phones that you can sale. Actually there could be a chance that in production some phones can break that you cannot sale. So if you would know how many phones has broken and total number of phones then you can calculate the phones that are not broken. And we all know non broken phones can be sold. But this non broken phone calculation method is very specific to only phone item. And brokenPhone attribute is only specific to the phone item so we cannot define it in our Item class. So what can we do?

You might think that you can solve it that way:
class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


phone1 = Item("Samsung", 1000, 5)
broken_phone = 1



//NOTE: The problem here is that we cannot access broken_phone attribute in our item class as we have not assigned it to the self keyword. 
SO what is the solution?

SOLUTION:
Here inheritance come into play:

We can create a class Phone and inherite it in Item class. In this way Item class will be our Parent class and Phone will be our child class. Moreover, In order to get access to all the attributes whether they are class attributes or instance attributes we have to use "super" class method. Due to this method we also won't have to hard code tha complete code of parent class in our child class and still we will be able to access all the attributes from our parent class. lets do that:

import csv


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"
    
    # self.__class__.__name__ is used to get the name of the class


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # calling to super function to get access to all the attributes of parent/Item class
        super().__init__(name, price, quantity)
        
        # applying validations

        assert broken_phones >= 0, f"Broken Phones {
            self.broken_phones} is not greater or equal to zero!"

    # assinging to self object
        self.broken_Phones = broken_phones
        
    def calculate_non_broken_phones(self):
        return print(f"Non Broken Phone {self.quantity - self.broken_Phones}") #<-----here we are accessing quantity attribute of our parent class in our child class




phone1 = Phone("Samsung", 1000, 5, 1)
phone2 = Phone("iPhone", 1300, 4, 1)
phone1.calculateTotalPrice() #<--------------here we are accessing the method of parent class on our child class
phone2.calculateTotalPrice()
phone1.calculate_non_broken_phones()
phone2.calculate_non_broken_phones()

print(Phone.all)


**NOTE**: The only thing we have to repeat is the name of attributes while calling the super function and __init__ method in our child class. You have to re-write the names of the attributes which you want to access from the parent class. Rest of the code from the parent class will be automatically get accessed by the super function.


**************************Getter and setters
What if any body comes and want to override some properties and we want them to restrict. How can we do that?
We can achieve this behaviour using @property method. Which means you cannot override them.
from item import Item
from phone import Phone

phone1 = Phone("Samsung", 1000, 5, 1)
phone1.name = "Huawei"

print(phone1.name)

#// output: Huawei

********Lets restrict its override

For this you have make some changes in your parent Item class

import csv


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.__name = name #<------------------------------------make changes here
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    @property
    # Property decorators means making name attribute a read only property
    def name(self):
        return self.__name #<------------------------------------make changes here

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"

    # self.__class__.__name__ is used to get the name of the class


phone1 = Phone("Samsung", 1000, 5, 1)
phone1.name = "Huawei"

print(phone1.name)  //you will get errors


*****************Setters (Encapsulation in action)
Encapsulation: In encapsulation we restrict our user to get direct access to some properties.

What if you really want to change it. No matters there are restrictions. Then you can do it by

import csv


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.__name = name
        self.price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    @property
    # Property decorators means making name attribute a read only property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculateTotalPrice(self):
        return print(f"Total price: {self.price*self.quantity}")

    def applyDiscount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"

    # self.__class__.__name__ is used to get the name of the class

phone1 = Phone("Samsung", 1000, 5, 1)
phone1.name = "Huawei"

print(phone1.name)

Now you will be able to override it

**NOTE** Restricting is basically where we have implemented encapsulation where we restrict our users to direct access to some properties
and doing __name etc. is called making attributes private

**************Price increment example: Encapsulation in action
import csv


class Item:
    # defining class attributes
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Applying asserting validation
        # here our validation goal is to make sure that user do not enter negative values of price and qty
        assert price >= 0, f"Price {
            self.__price} is not greater or equal to zero!"
        assert quantity >= 0, f"Price {
            self.quantity} is not greater or equal to zero!"

        # Assigning attributes to self
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # appending each instance into the all array
        Item.all.append(self)

    @property
    # Property decorators means making name attribute a read only property
    def name(self):
        return self.__name

    @property #<----------------------------Here we are restricting our direct access to the price
    # Property decorators means making name attribute a read only property
    def price(self):
        return self.__price

    def apply_increment(self, increment_by_value): #<------------creating a method to manipulate price 
         self.__price = self.price + self.__price * increment_by_value

    @name.setter
    def name(self, value):
        self.__name = value

    def calculateTotalPrice(self):
        return print(f"Total price: {self.__price*self.quantity}")

    def applyDiscount(self):
        return self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # here cls is that Item calss itself on which the instatiate_from_Csv method is getting called
        with open('./items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            # print(item.get('name'))
            # print(item.get('price'))
            # print(item.get('quantity'))

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # here we are making a count
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price}, {self.quantity})"

    # self.__class__.__name__ is used to get the name of the class

	

phone1 = Phone("Samsung", 1000, 5, 1)
phone1.apply_increment(0.2)

print(phone1.price)

# here we have not allowed our user to access the price directly to manipulate it but we have used method to increment the value only.

#************Abstraction, Private method, public method
Abstraction is simply means that hiding the unnecessary information from the user (here user means the person who is gonna use our classes) and only showing the necessary information
For example: Creating a class for sending emails. There is big huge process behind sending emails such as connecting to SMTP server, preparing the message body etc. 

def __connect_to_SMTP(self):
        pass
    def __prepare_message_body(self):
        pass
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect_to_SMTP()
        self.__prepare_message_body
        self.__send()
        return "Email has sent successfully!"

phone1 = Phone("Samsung", 1000, 5, 1)

print(phone1.send_email())


# here user dont know about the methods that are being used inside send_email method. Not the user can even access to those methods. The reason is that all the methods inside send_email method are private methods. Means that they are only accessible inside the class. In python double under score is used to define the private attributes. Here send_email is a public attribute. This is how we abstract our methods from the user.

*****************Inheritance
We have already seen above inheritance in action. Inheritance is very powerful to create reuseable piece of code, You can create a child class having all the properties of the parent class along with some of its specific properites. You can make as many child of a parent class you want to make your code reuseable.


************Polymorphism
Polymorphism means that many forms of the same function or class
Example:
Length function in python

name ="Jim"
print(len(name)) //output = 3

list = ["sam" , "john"]
print(len(list)) //output = 2


As you can see here the function is same and it is taking diff types of arguments. but it is giving the output accordingly. As you can see for string it is counting letters and for list it is counting the number of elements. This is a perfect example of polymorphism.


Polymorphism is implemented with inheritance where you inherite classes and take work accordingly.


Method Overloading: 
Method Overloading is an example of Compile time polymorphism. In this, more than one method of the same class shares the same method name having different signatures. Method overloading is used to add more to the behavior of methods and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. We may overload the methods but can only use the latest defined method.
```bash
# Function to take multiple arguments 
def add(datatype, *args): 

	# if datatype is int 
	# initialize answer as 0 
	if datatype =='int': 
		answer = 0
		
	# if datatype is str 
	# initialize answer as '' 
	if datatype =='str': 
		answer ='' 

	# Traverse through the arguments 
	for x in args: 

		# This will do addition if the 
		# arguments are int. Or concatenation 
		# if the arguments are str 
		answer = answer + x 

	print(answer) 

# Integer 
add('int', 5, 6) 

# String 
add('str', 'Hi ', 'Geeks') 
```

Method Overriding: 
Method overriding is an example of run time polymorphism. In this, the specific implementation of the method that is already provided by the parent class is provided by the child class. It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding. In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.

```bash
class A:

	def fun1(self):
		print('feature_1 of class A')
		
	def fun2(self):
		print('feature_2 of class A')
	

class B(A):
	
	# Modified function that is 
	# already exist in class A
	def fun1(self):
		print('Modified feature_1 of class A by class B') 
		
	def fun3(self):
		print('feature_3 of class B')
		

# Create instance
obj = B()
	
# Call the override function
obj.fun1()

```

