from item import Item


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
        return print(f"Non Broken Phone {self.quantity - self.broken_Phones}")
