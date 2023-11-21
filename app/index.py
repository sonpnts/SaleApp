from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login
from flask_login import login_user
import math


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    cates = dao.load_catelogies()
    products = dao.load_product(kw=kw,cate_id=cate_id,page=page)

    total = dao.count_product()

    return render_template('index.html', catelogies = cates, product = products,
                           pages=math.ceil(total/app.config['PAGE_SIZE']))

@app.route('/api/cart', methods=['post'])
def add_cart():

    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get('id'))

    if id in cart:
        cart[id]["quantity"]=cart[id]["quantity"] + 1

    else:
        cart[id] = {
            "id": id,
            "name":data.get("name"),
            "price":data.get("price"),
            "quantity":1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user=dao.auth_user(username=username,password=password)
    # try:
    #     if user:
    #         login_user(user=user)
    #         return redirect('/admin')
    #
    # except Exception as ex:
    #     return(ex)
    # #
    #     return redirect('/admin/login')
    if user:
        login_user(user=user)

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__=='__main__':
    from app import admin
    app.run(debug=True)