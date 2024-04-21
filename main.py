from item import Item
from phone import Phone


phone1 = Phone("Samsung", 1000, 5, 1)
phone1.name = "Huawei"
phone1.apply_increment(0.2)

print(phone1.send_email())

# print(phone1.price)
