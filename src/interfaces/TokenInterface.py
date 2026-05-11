import abc


class TokenInterface(abc.ABC):

    @abc.abstractmethod
    def generate_token(self, user_id):
        pass
