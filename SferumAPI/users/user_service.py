"""
Модуль работы с пользователями

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from ..models import UserCredentials, AnonCredentials
from .user_auth import UserAuth
from .anon_auth import AnonAuth


class UserService:
    """Сервис работы с пользователем"""

    def __init__(self, remixdsid: str):
        self.__user_auth = None
        self.__anon_auth = None
        self.__user = None
        self.__anon = None
        self.__remixdsid = remixdsid

    def authorize(self):
        """Авторизация"""
        self.__user_auth = UserAuth(remixdsid=self.__remixdsid)
        self.__user = self.__user_auth.authorize()
        self.__anon_auth = AnonAuth(access_token=self.__user.access_token)
        self.__anon = self.__anon_auth.authorize()

    def get_user(self) -> UserCredentials:
        """Получить данные пользователя"""
        if not self.__user:
            self.authorize()
        return self.__user

    def get_anon(self) -> AnonCredentials:
        """Получить данные сессии для звонков"""
        if not self.__anon:
            self.authorize()
        return self.__anon
