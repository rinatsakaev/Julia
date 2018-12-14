from flask import Blueprint, render_template, request, redirect, url_for
from Models.User import User
from Helper import get_receipt
import random
from app import db
home_controller = Blueprint('home_controller', __name__)


@home_controller.route('/')
def index():
    receipts = []
    for receipt_id in random.sample(range(500, 1000), 10):
        receipt = get_receipt(f"https://www.russianfood.com/recipes/recipe.php?rid={receipt_id}")
        if receipt:
            receipts.append(receipt)
    return render_template("index.html", receipts = receipts)


@home_controller.route('/users')
def users():
    return render_template("users.html", users=User.query.all())


@home_controller.route('/users/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        login = request.form['username']
        email = request.form['email']
        new_user = User(login, email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_controller.users'))
