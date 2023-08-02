from marshmallow import Schema, fields, post_load
from api.models.models import Restaurant, Promotion, MenuItem, StaffMapping, Review, Administrator, Order, OrderItem, PaymentTransaction, Customer, LoyaltyProgram

class RestaurantSchema(Schema):
    restaurant_id = fields.Integer()
    admin_id = fields.Integer()
    restaurant_name = fields.String(allow_none=False)
    email = fields.String(allow_none=False)
    password = fields.String(allow_none=False)
    location = fields.String(allow_none=False)
    ambience = fields.String(allow_none=False)
    cuisines_offered = fields.String(allow_none=False)
    operating_hours = fields.String(allow_none=False)
    contact_info = fields.String(allow_none=False)

    @post_load
    def make_restaurant(self, data, **kwargs):
        return Restaurant(**data)


class PromotionSchema(Schema):
    promotion_id = fields.Integer()
    restaurant_id = fields.Integer()
    promotion_name = fields.String(allow_none=False)
    promotion_description = fields.String(allow_none=False)
    start_date = fields.String(allow_none=False)
    end_date = fields.String(allow_none=False)
    discount_amount = fields.String(allow_none=False)

    @post_load
    def make_promotion(self, data, **kwargs):
        return Promotion(**data)


class MenuItemSchema(Schema):
    item_id = fields.Integer()
    restaurant_id = fields.Integer()
    item_name = fields.String(allow_none=False)
    item_category = fields.String(allow_none=False)
    item_description = fields.String(allow_none=False)
    price = fields.Integer()
    customization_options = fields.String(allow_none=False)

    @post_load
    def make_menu_item(self, data, **kwargs):
        return MenuItem(**data)


class StaffMappingSchema(Schema):
    staff_id = fields.Integer()
    restaurant_id = fields.Integer()
    staff_name = fields.String(allow_none=False)
    staff_role = fields.String(allow_none=False)

    @post_load
    def make_staff_map(self, data, **kwargs):
        return StaffMapping(**data)


class ReviewSchema(Schema):
    review_id = fields.Integer()
    user_id = fields.Integer()
    restaurant_id = fields.Integer()
    review_text = fields.String(allow_none=False)
    review_rating = fields.Integer()

    @post_load
    def make_review(self, data, **kwargs):
        return Review(**data)


class AdministratorSchema(Schema):
    admin_id = fields.Integer()
    admin_username = fields.String(allow_none=False)
    admin_email = fields.String(allow_none=False)
    admin_password = fields.String(allow_none=False)

    @post_load
    def make_administrator(self, data, **kwargs):
        return Administrator(**data)


class OrderSchema(Schema):
    order_id = fields.Integer()
    user_id = fields.Integer()
    restaurant_id = fields.Integer()
    order_status = fields.String(allow_none=False)
    order_total = fields.Integer()
    order_date = fields.String(allow_none=False)

    @post_load
    def make_order(self, data, **kwargs):
        return Order(**data)


class OrderItemSchema(Schema):
    order_item_id = fields.Integer()
    order_id = fields.Integer()
    item_id = fields.Integer()
    quantity = fields.Integer()
    subtotal = fields.Integer()

    @post_load
    def make_order_item(self, data, **kwargs):
        return OrderItem(**data)


class PaymentTransactionSchema(Schema):
    transaction_id = fields.Integer()
    order_id = fields.Integer()
    payment_date = fields.String(allow_none=False)
    payment_amount = fields.Integer()
    payment_status = fields.String(allow_none=False)

    @post_load
    def make_payment_transaction(self, data, **kwargs):
        return PaymentTransaction(**data)


class CustomerSchema(Schema):
    customer_id = fields.Integer()
    admin_id = fields.Integer()
    role = fields.String(allow_none=False)
    username = fields.String(allow_none=False)
    email = fields.String(allow_none=False)
    password = fields.String(allow_none=False)
    phone_number = fields.String(allow_none=False)
    address = fields.String(allow_none=False)

    @post_load
    def make_customer_schema(self, data, **kwargs):
        return Customer(**data)


class LoyaltyProgramSchema(Schema):
    loyalty_program_id = fields.Integer()
    customer_id = fields.Integer()
    loyalty_points = fields.Integer()

    @post_load
    def make_loyalty_program(self, data, **kwargs):
        return LoyaltyProgram(**data)

class UserSchema(Schema):
    id = fields.String()
    name = fields.String()
    email = fields.String()
    emailVerified = fields.DateTime()
    image = fields.String()
    role = fields.String()
