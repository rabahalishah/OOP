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

    @property
    # Property decorators means making name attribute a read only property
    def price(self):
        return self.__price

    def apply_increment(self, increment_by_value):
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
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price}, {self.quantity})"

    # self.__class__.__name__ is used to get the name of the class
