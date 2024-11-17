"""
Модуль работы с звонками

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class CallStrategy(ABC):
    """Стратегия звонков"""

    @abstractmethod
    def start(self) -> T:
        """Создание звонка"""

    @abstractmethod
    def end(self) -> T:
        """Завершение звонока"""
