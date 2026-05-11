import abc


class AuthRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def create_user(self, username, password_hash):
        pass

    @abc.abstractmethod
    def get_user(self, username):
        pass

    @abc.abstractmethod
    def get_by_email(self, email):
        pass
