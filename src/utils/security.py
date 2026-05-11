import bcrypt

from src.interfaces.password_service_inferface import PasswordServiceInterface


class PasswordService(PasswordServiceInterface):

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
