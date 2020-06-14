from flask import Blueprint, render_template


product = Blueprint(
    'product',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@product.route('/')
def store():
    return render_template('product/store.html')
