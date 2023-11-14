import hashlib

from app.models import Category, Product, User

def load_catelogies():
    return Category.query.all()



def load_product(kw):

    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()
