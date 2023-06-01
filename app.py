from flask import Flask
from flask_restx import Api

from configs.default_config import Config
from setup_db import db, SQLAlchemy
from views.schedule import schedule_ns


def create_application(config: Config, database: SQLAlchemy) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config) # Берёт конфигурацию из конфига для приложения
    application.app_context().push() # Применяет конфигурацию из конфига в приложении
    register_extensions(application, database)
    return application

def register_extensions(application: Flask, database: SQLAlchemy) -> None:
    database.init_app(application)
    api = Api(application)
    api.add_namespace(schedule_ns)

def create_db(application: Flask, database: SQLAlchemy) -> None:
    with application.app_context():
        database.create_all()


app_config = Config()
app = create_application(app_config, db)
create_db(app, db)

if __name__ == "__main__":
    app.run()
