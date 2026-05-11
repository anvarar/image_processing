from src.db.entity.User import User
from src.interfaces.AuthRepositoryInterface import AuthRepositoryInterface


class UserData(AuthRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def get_user(self, email):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db, email, password):
        user = User(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_email(self, email):
        pass
