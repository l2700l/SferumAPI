"""
messages models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import dataclasses


@dataclasses.dataclass
class Message:
    def __init__(self, **kwargs) -> None:
        self.cmid = kwargs.get("cmid")
        self.message_id = kwargs.get("message_id")
