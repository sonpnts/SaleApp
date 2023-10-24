from flask import Flask, render_template, request
import dao
app = Flask (__name__)


@app.route('/')

def index():
    kw = request.args.get('kw')
    cates = dao.load_catelogies()
    products = dao.load_product(kw=kw)

    return render_template('index.html', catelogies = cates, product = products)


if __name__=='__main__':
    app.run(debug=True)