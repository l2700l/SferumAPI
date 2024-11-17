"""
user models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from dataclasses import dataclass


@dataclass
class UserCredentials:
    user_id: int
    profile_type: int
    access_token: str
    expires: int
