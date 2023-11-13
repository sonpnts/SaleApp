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
