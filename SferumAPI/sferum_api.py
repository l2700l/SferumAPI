"""
Sferum API

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from .users import UserService
from .messages import MessageService
from .calls import CallService
from .channels import ChannelService

class SferumAPI:
    """API-обертка для работы со Сферумом"""

    def __init__(self, remixdsid: str):
        self.users = UserService(remixdsid=remixdsid)
        self.users.authorize()
        self.messages = MessageService(self.users.get_user())
        self.calls = CallService(self.users.get_user(), self.users.get_anon())
        self.channels = ChannelService(self.users.get_user())
