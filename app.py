from flask import Flask
from database import db
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db.init_app(app)

from Controllers.HomeController import home_controller
app.register_blueprint(home_controller)

if __name__ == '__main__':
    app.run()
