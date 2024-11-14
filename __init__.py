from flask import Flask

cart = Flask(__name__)
cart.config['SECRET_KEY'] = 'your_secret_key'

from cart import routescart  # из проекта cart импортируем файл routescart, в котором будем прописывать пути