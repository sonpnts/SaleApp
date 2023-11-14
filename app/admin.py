from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product
from flask_login import logout_user
from flask import redirect


class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

class MyProductView(ModelView):
    column_list = ['name', 'price','category']
    column_display_pk = False
    column_searchable_list = ['name']
    column_filters = ['price']
    can_export = True
    can_view_details = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']

class MyLogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

# class MyModelView(ModelView):
#     can_export = True
#     can_view_details = True

admin = Admin(app=app, name = "QUẢN TRỊ BÁN HÀNG", template_mode='bootstrap4')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name="Thống kê báo cáo"))
admin.add_view(MyLogoutView(name="Đăng xuất"))