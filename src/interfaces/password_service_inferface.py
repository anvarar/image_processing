import abc


class PasswordServiceInterface(abc.ABC):

    @abc.abstractmethod
    def hash_password(self, password):
        pass

    @abc.abstractmethod
    def verify_password(self, password, hashed_password):
        pass
