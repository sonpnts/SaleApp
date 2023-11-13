from sqlalchemy import Column, Integer, String , Float, ForeignKey
from app import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    image=Column(String(100), default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dperson%2Bicon&psig=AOvVaw2Sy_coSUaFSSXd2dWwRtEN&ust=1699974243255000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPDl_tifwYIDFQAAAAAdAAAAABAE')
    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__= 'catelogy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable= False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default= 0)
    image = Column(String (100))
    category_id= Column(Integer, ForeignKey(Category.id),nullable=False)

if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.create_all()
        c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        p1 = Product(name="Iphone 12", price=150000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=1)
        p2 = Product(name="Ipad Pro 2023", price=200000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(p1)
        db.session.add(p2)

        db.session.commit()
