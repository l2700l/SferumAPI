"""
Классы для работы с ответами от API

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import dataclasses

from typing import TypeVar

T = TypeVar("T")


@dataclasses.dataclass
class Response:
    """Обертка для response"""

    response: T
