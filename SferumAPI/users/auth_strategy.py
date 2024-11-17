"""
Модуль работы с пользователями

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class AuthStrategy(ABC):
    """Стратегия авторизации"""

    @abstractmethod
    def authorize(self) -> T:
        """Авторизация"""
