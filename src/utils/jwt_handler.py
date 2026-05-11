from datetime import datetime, timedelta
import jwt

from src.interfaces.TokenInterface import TokenInterface

SECRET = "secret_key"


class TokenService(TokenInterface):

    def generate_token(self, user_id):
        payload = {
            "user_id": user_id,
            "expiration": datetime.utcnow() + timedelta(hours=2)
        }
        return jwt.encode(payload, SECRET, algorithm="HS256")
