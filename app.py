from flask import Flask
from flask_restx import Api

from configs.default_config import Config
from setup_db import db
from views import note_ns


app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()

db.init_app(app)

api = Api(app)
api.add_namespace(note_ns)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
