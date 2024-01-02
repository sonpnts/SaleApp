import hashlib

from app.models import Category, Product, User, Receipt, ReceiptDetails
from app import app,db
import cloudinary.uploader
from flask_login import current_user
from sqlalchemy import func

def load_catelogies():
    return Category.query.all()



def load_product(kw=None, cate_id=None, page=None):

    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    if  cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page-1) * page_size
        return products.slice(start, start + page_size)

    return products.all()

def count_product():
    return Product.query.count()

def get_user_by_id(user_id):
    return User.query.get(user_id)



def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password)

    if avatar:
        res= cloudinary.uploader.upload(avatar)
        print(res)
        u.avatar = res['secure_url']


    db.session.add(u)
    db.session.commit()


def add_recipt(cart):
    if cart:
        r = Receipt(user = current_user)
        db.session.add(r)

        for item in cart.values():
            rd = ReceiptDetails(quantity=item['quantity'], price=item['price'], receipt=r, product_id=item['id'])
            db.session.add(rd)

        db.session.commit()

def count_products_by_cate():
    return db.session.query(Category.id,Category.name, func.count(Product.id))\
        .join(Product, Product.category_id==Category.id, isouter=True).group_by(Category.id).all()



if __name__=='__main__':
    with app.app_context():
        print(count_products_by_cate())
