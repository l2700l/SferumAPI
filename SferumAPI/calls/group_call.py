"""
Модуль работы с звонками

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import uuid

import requests
from .call_strategy import CallStrategy
from ..models import CallStart, Response


class GroupCall(CallStrategy):
    """Реализация групповых звонков"""

    def __init__(self, session_key: str, access_token: str):
        self.__conversation_id = None
        self.__session_key = session_key
        self.__access_token = access_token

    def start(self):
        if self.__conversation_id is not None:
            raise RuntimeError("Call is already in progress")
        try:
            self.__conversation_id = str(uuid.uuid4())
            url = "https://api.mycdn.me/fb.do"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "conversationId": self.__conversation_id,
                "isVideo": "false",
                "protocolVersion": "5",
                "createJoinLink": "true",
                "payload": '{"is_video":false,"with_join_link":true,"join_by_link":true,"community_user_id":0,"caller_app_id":6287487}',
                "method": "vchat.startConversation",
                "format": "JSON",
                "application_key": "CFJCCIJGDIHBABABA",
                "session_key": self.__session_key,
                "onlyAdminCanShareMovie": "false",
            }
            response = requests.post(url, headers=headers, data=data, timeout=3)
            response.raise_for_status()
            return CallStart(**response.json())
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")

    def end(self):
        if self.__conversation_id is None:
            raise ReferenceError("Call is not already in progress")
        try:
            url = "https://api.vk.me/method/messages.forceCallFinish?v=5.241"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "access_token": self.__access_token,
                "call_id": self.__conversation_id,
            }
            response = requests.post(url, headers=headers, data=data, timeout=3)
            response.raise_for_status()
            self.__conversation_id = None
            return Response[int](**response.json())
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")
