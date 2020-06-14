from flask import Blueprint, render_template


cart = Blueprint(
    'cart',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@cart.route('/')
def cart_summary():
    return render_template('cart/cart.html')
