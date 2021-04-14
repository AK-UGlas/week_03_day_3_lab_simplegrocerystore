from flask import render_template
from app import app
from models.online_groceries import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders, order_len=len(orders))

@app.route('/orders/<index>')
def display_order(index):
    order = orders[int(index)]
    return render_template('order.html', title='Specific order', order_to_display=order)