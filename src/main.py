from flask import Flask

from src.db.db_config import Base, engine
from src.endpoints import api_blueprint


def init_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
    application = init_app()
    application.run(debug=True)
