from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database_engine import engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    restaurant_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('administrator.admin_id'))
    restaurant_name = Column(String)
    email = Column(String)
    password = Column(String)
    location = Column(String)
    ambience = Column(String)
    cuisines_offered = Column(String)
    operating_hours = Column(String)
    contact_info = Column(String)
    promotions = relationship('Promotion', back_populates='restaurant')
    menu_items = relationship('MenuItem', back_populates='restaurant')
    staff_mapping = relationship('StaffMapping', back_populates='restaurant')
    reviews = relationship('Review', back_populates='restaurant')
    orders = relationship('Order', back_populates='restaurant')
    customers = relationship('Customer', back_populates='restaurant')

class Promotion(Base):
    __tablename__ = 'promotion'
    promotion_id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    promotion_name = Column(String)
    promotion_description = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    discount_amount = Column(String)
    restaurant = relationship('Restaurant', back_populates='promotions')

class MenuItem(Base):
    __tablename__ = 'menu_item'
    item_id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    item_name = Column(String)
    item_category = Column(String)
    item_description = Column(String)
    price = Column(Integer)
    customization_options = Column(String)
    restaurant = relationship('Restaurant', back_populates='menu_items')

class StaffMapping(Base):
    __tablename__ = 'staff_mapping'
    staff_id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    staff_name = Column(String)
    staff_role = Column(String)
    restaurant = relationship('Restaurant', back_populates='staff_mapping')

class Review(Base):
    __tablename__ = 'review'
    review_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('customer.customer_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    review_text = Column(String)
    review_rating = Column(Integer)
    restaurant = relationship('Restaurant', back_populates='reviews')

class Administrator(Base):
    __tablename__ = 'administrator'
    admin_id = Column(Integer, primary_key=True)
    admin_username = Column(String)
    admin_email = Column(String)
    admin_password = Column(String)
    restaurants = relationship('Restaurant', back_populates='admin')

class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('customer.customer_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    order_status = Column(String)
    order_total = Column(Integer)
    order_date = Column(String)
    items = relationship('OrderItem', back_populates='order')
    payments = relationship('PaymentTransaction', back_populates='order')
    restaurant = relationship('Restaurant', back_populates='orders')

class OrderItem(Base):
    __tablename__ = 'order_item'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.order_id'))
    item_id = Column(Integer, ForeignKey('menu_item.item_id'))
    quantity = Column(Integer)
    subtotal = Column(Integer)
    order = relationship('Order', back_populates='items')

class PaymentTransaction(Base):
    __tablename__ = 'payment_transaction'
    transaction_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.order_id'))
    payment_date = Column(String)
    payment_amount = Column(Integer)
    payment_status = Column(String)
    order = relationship('Order', back_populates='payments')

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('administrator.admin_id'))
    role = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    phone_number = Column(String)
    address = Column(String)
    orders = relationship('Order', back_populates='customer')
    restaurant = relationship('Restaurant', back_populates='customers')

class LoyaltyProgram(Base):
    __tablename__ = 'loyalty_program'
    loyalty_program_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    loyalty_points = Column(Integer)
    customer = relationship('Customer', back_populates='loyalty_program')

Base.metadata.create_all(engine)
