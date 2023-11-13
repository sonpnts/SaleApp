from flask import render_template, request
import dao
from app import app, login


@app.route('/')

def index():
    kw = request.args.get('kw')
    cates = dao.load_catelogies()
    products = dao.load_product(kw=kw)

    return render_template('index.html', catelogies = cates, product = products)

@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        return 'Đăng nhập thành công'

    else:
        return 'Đăng nhập thất bại'

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__=='__main__':
    from app import admin
    app.run(debug=True)