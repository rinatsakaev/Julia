from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from database import db
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db.init_app(app)

from Models.User import User
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    print("rn")
    manager.run()