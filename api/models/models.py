from api.database import db

class Restaurant(db.Model):
    restaurant_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('administrator.admin_id'))
    restaurant_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    location = db.Column(db.String)
    ambience = db.Column(db.String)
    cuisines_offered = db.Column(db.String)
    operating_hours = db.Column(db.String)
    contact_info = db.Column(db.String)
    promotions = db.relationship('Promotion', back_populates='restaurant')
    menu_items = db.relationship('MenuItem', back_populates='restaurant')
    staff_mapping = db.relationship(
        'StaffMapping', back_populates='restaurant')
    reviews = db.relationship('Review', back_populates='restaurant')
    orders = db.relationship('Order', back_populates='restaurant')
    customers = db.relationship('Customer', back_populates='restaurant')


class Promotion(db.Model):
    promotion_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    promotion_name = db.Column(db.String)
    promotion_description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    discount_amount = db.Column(db.String)
    restaurant = db.relationship('Restaurant', back_populates='promotions')


class MenuItem(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    item_name = db.Column(db.String)
    item_category = db.Column(db.String)
    item_description = db.Column(db.String)
    price = db.Column(db.Integer)
    customization_options = db.Column(db.String)
    restaurant = db.relationship('Restaurant', back_populates='menu_items')


class StaffMapping(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    staff_name = db.Column(db.String)
    staff_role = db.Column(db.String)
    restaurant = db.relationship('Restaurant', back_populates='staff_mapping')


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    review_text = db.Column(db.String)
    review_rating = db.Column(db.Integer)
    restaurant = db.relationship('Restaurant', back_populates='reviews')


class Administrator(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_username = db.Column(db.String)
    admin_email = db.Column(db.String)
    admin_password = db.Column(db.String)
    restaurants = db.relationship('Restaurant', back_populates='admin')


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    order_status = db.Column(db.String)
    order_total = db.Column(db.Integer)
    order_date = db.Column(db.String)
    items = db.relationship('OrderItem', back_populates='order')
    payments = db.relationship('PaymentTransaction', back_populates='order')
    restaurant = db.relationship('Restaurant', back_populates='orders')


class OrderItem(db.Model):
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.item_id'))
    quantity = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)
    order = db.relationship('Order', back_populates='items')


class PaymentTransaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    payment_date = db.Column(db.String)
    payment_amount = db.Column(db.Integer)
    payment_status = db.Column(db.String)
    order = db.relationship('Order', back_populates='payments')


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('administrator.admin_id'))
    role = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    orders = db.relationship('Order', back_populates='customer')
    restaurant = db.relationship('Restaurant', back_populates='customers')


class LoyaltyProgram(db.Model):
    loyalty_program_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    loyalty_points = db.Column(db.Integer)
    customer = db.relationship('Customer', back_populates='loyalty_program')
