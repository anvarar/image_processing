from flask import Flask

from src.db.db_config import Base, engine


def init_app():
    app = Flask(__name__)
    return app


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
    application = init_app()
    application.run(debug=True)
