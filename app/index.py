from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login, db
from flask_login import login_user, logout_user
import math


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    cates = dao.load_catelogies()
    products = dao.load_product(kw=kw, cate_id=cate_id, page=page)

    total = dao.count_product()

    return render_template('index.html', catelogies=cates, product=products,
                           pages=math.ceil(total / app.config['PAGE_SIZE']))

@app.context_processor
def common_resp():
    return {
        'catelogies': dao.load_catelogies(),
        'cart': utils.count_cart(session.get('cart'))
    }


@app.route('/api/cart', methods=['post'])
def add_cart():
    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get('id'))

    if id in cart:
        cart[id]["quantity"] = cart[id]["quantity"] + 1

    else:
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart']=cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart']=cart

    return jsonify(utils.count_cart(cart))


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route('/cart')
def cart_list():
    return render_template('cart.html')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route("/login", methods=['get','post'])
def login_user_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

        next = request.args.get('next')
        return redirect("/" if next is None else next)
    return render_template ("login.html")


@app.route('/logout')
def process_logout_user():
    logout_user()
    return redirect("/login")

@app.route('/register',  methods=['get','post'])
def register_user():
    err_msg = ""
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        if password.__eq__(confirm):
            try:
                dao.add_user(name=request.form.get('name'),
                             username=request.form.get('username'),
                            password=password,
                             avatar=request.files.get('avatar'))
            except:
                err_msg = 'Hệ thống đang bận, vui lòng thử lại sau!'
            else:
                return redirect('/login')
        else:
            err_msg = "Mật khẩu không khớp! Vui lòng nhập lại"
    return render_template('register.html', err_msg=err_msg)

@app.route('/pay', methods=['post'])
def pay():
    try:
        dao.add_recipt(session.get('cart'))
    except:
        return jsonify({'status':500,'err_msg': 'Hệ thống đang bận, vui lòng thử lại sau!'})
    else:
        del session['cart']
        return jsonify({'status':200})



if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
