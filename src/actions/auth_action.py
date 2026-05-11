from src.interfaces.AuthRepositoryInterface import AuthRepositoryInterface
from src.interfaces.TokenInterface import TokenInterface
from src.interfaces.password_service_inferface import PasswordServiceInterface


class AuthAction:
    def __init__(self,
                 task_repo: AuthRepositoryInterface,
                 password_service: PasswordServiceInterface,
                 token_service: TokenInterface):
        self.task_repo = task_repo
        self.password_service = password_service
        self.token_service = token_service

    def _check_user_exists(self, username):
        if self.task_repo.get_user(username):
            raise Exception("user already exists!")

    def _check_credential_valid(self, user, password):
        if not user:
            raise Exception("Invalid credentials!")
        if not self.password_service.verify_password(password, user.password):
            raise Exception("Invalid credentials!")

    def _get_user_by_email(self, email):
        return self.task_repo.get_by_email(email)

    def signup(self, username, password):
        self._check_user_exists(username)
        password_hash = self.password_service.hash_password(password)
        return self.task_repo.create_user(username, password_hash)

    def login(self, email, password):
        user = self._get_user_by_email(email)
        self._check_credential_valid(user, password)
        return {"token": self.token_service.generate_token(user.id)}
