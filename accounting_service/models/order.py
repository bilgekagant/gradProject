from app import db
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    order_type = db.Column(db.Enum('buy', 'sell', name='order_type'), nullable=False)
    product_details = db.Column(JSONB)
    price = db.Column(db.Numeric, nullable=False)
    status = db.Column(db.Enum('open', 'matched', 'closed', name='order_status'), nullable=False)

    def __init__(self, user_id, order_type, product_details, price, status):
        self.user_id = user_id
        self.order_type = order_type
        self.product_details = product_details
        self.price = price
        self.status = status