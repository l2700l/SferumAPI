"""
Модуль работы с звонками

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from ..models import AnonCredentials, UserCredentials
from .group_call import GroupCall
from .peer_call import PeerCall


class CallService:
    """Служба работы с звонками"""

    def __init__(self, user: UserCredentials, session: AnonCredentials):
        self.__user = user
        self.__session = session
        self.group = GroupCall(
            session_key=self.__session.session_key,
            access_token=self.__user.access_token,
        )
        self.peer = PeerCall(
            session_key=self.__session.session_key, session_uid=self.__session.uid
        )
