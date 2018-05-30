# -*- coding: utf-8 -*-
from pony.orm import Database, Required, Optional, Set, PrimaryKey
from datetime import datetime

db = Database()




class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    description = Optional(str)
    unit = Required(str)
    price = Required(float)
    #alt_categories = Set('Category')
    #anmount = int # кол-во товара магазина
    history = Set('ProductHistory')
    caritems = Optional('CartItems')
    #orderitem = Set('OrderItem')

class ProductHistory(db.Entity):
    """ История изменения продукта"""
    product = Required('Product')
    created = Required(datetime, default = datetime.now)
    price = Required(float)

class Category(db.Entity):
    """Категория товара"""
    title = Required(str)
    parent = 'Category'
    products = Set(Product)


class Customer(db.Entity):
    """Покупатель"""
    email = Required(str)
    phone = Optional(str)
    name = Required(str)
    address = Set('Address')
    cart = Optional('Cart')
    order = Optional('Order')


class Address(db.Entity):
    """Адрес"""
    customer = 'Customer'
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Optional('Customer') or None
    products = Set('CartItems')

class CartItems(Product):
    """Элемент корзины"""
    cart = Optional('Cart')
    product = Set('Product')
    amount = Required(int) # 1 единица товара


class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    created  = Required(datetime, default = datetime.now)
    products = Set('OrderItem')
    status = Required('Status')
    #cost =

class Status(db.Entity):
    """Статус"""
    name = Required(str)
    order = Optional('Order')

class OrderItem:
    """Товар (одна позиция) в заказе"""
    order = Set('Order')
    #product = Set('Product')
    amount = Required(int) # 1 единица товара

class Menu:
    """Меню"""


db.bind(provider = 'sqlite', filename = 'shop.sqlite', create_db = True)
db.generate_mapping(create_tables = True)

with db.session():
    prod_1 = Product(
        unit = 'box pack',
        price = 1000,
        description = 'The best of the best',
        title = 'CPU',
        )
