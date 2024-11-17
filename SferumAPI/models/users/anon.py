"""
user models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from dataclasses import dataclass
from json_to_models.dynamic_typing import IntString


@dataclass
class AnonCredentials:
    uid: IntString
    session_key: str
    session_secret_key: str
    api_server: str
    activated_profile: bool
