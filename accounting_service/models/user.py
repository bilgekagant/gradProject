from app import db
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile = db.Column(JSONB)
    inventory_items = db.Column(db.ARRAY(UUID(as_uuid=True)))

    def __init__(self, email, password_hash, username, profile):
        self.email = email
        self.password_hash = password_hash
        self.username = username
        self.profile = profile