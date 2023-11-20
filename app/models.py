from sqlalchemy import Column, Integer, String , Float, ForeignKey, Enum, Boolean
from app import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    image=Column(String(255), default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dperson%2Bicon&psig=AOvVaw2Sy_coSUaFSSXd2dWwRtEN&ust=1699974243255000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPDl_tifwYIDFQAAAAAdAAAAABAE')
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

        import hashlib

        u = User(name='Admin', username='admin',
                 password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),user_role = UserRoleEnum.ADMIN)

        db.session.add(u)
        db.session.commit()


        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # p1 = Product(name="Iphone 12", price=150000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=1)
        # p2 = Product(name="Ipad Pro 2023", price=200000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=2)
        # p3 = Product(name="Iphone 12", price=150000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=1)
        # p4 = Product(name="Ipad Pro 2023", price=200000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=2)
        # p5 = Product(name="Iphone 12", price=150000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=1)
        # p6 = Product(name="Ipad Pro 2023", price=200000, image="https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp", category_id=2)
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add_all([p1, p2, p3, p4, p5,p6])

        # db.session.commit()
