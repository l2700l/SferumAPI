"""
Модуль работы с звонками

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import uuid
import json
from websockets.sync.client import connect
import websockets
import requests
from .call_strategy import CallStrategy
from ..models import CallStart, PeerCallEnd


class PeerCall(CallStrategy):
    """Реализация личных звонков"""

    def __init__(self, session_key: str, session_uid: str):
        self.__conversation_id = None
        self.__conversation_token = None
        self.__peer_id = None
        self.__session_key = session_key
        self.__session_uid = session_uid

    def set_peer_id(self, peer_id: int):
        """Установка пользователя для звонка"""
        try:
            url = "https://api.mycdn.me/fb.do"

            headers = {
                "accept": "*/*",
                "accept-language": "ru,en-US;q=0.9,en;q=0.8,ja;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "dnt": "1",
                "origin": "https://web.vk.me",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://web.vk.me/",
                "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            }

            data = {
                "externalIds": f'[{{"id":"{peer_id}","ok_anonym":false}}]',
                "method": "vchat.getOkIdsByExternalIds",
                "format": "JSON",
                "application_key": "CFJCCIJGDIHBABABA",
                "session_key": self.__session_key,
            }

            response = requests.post(url, headers=headers, data=data, timeout=3)

            self.__peer_id = response.json()["ids"][0]["ok_user_id"]
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")

    def start(self):
        if self.__conversation_id is not None or self.__peer_id is None:
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
                "uids": self.__peer_id,
            }
            response = requests.post(url, headers=headers, data=data, timeout=3)
            response.raise_for_status()
            self.__conversation_token = response.json()["token"]
            return CallStart(**response.json())
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")

    def end(self):
        try:
            url = (
                f"wss://videowebrtc.okcdn.ru/ws?"
                f"userId={self.__session_uid}&entityType=USER&conversationId={self.__conversation_id}&"
                f"token={self.__conversation_token}&ispAsNo=9123&ispAsOrg=TimeWeb%20Ltd.&locCc=NL&"
                f"locReg=07&platform=WEB&appVersion=1.1&version=5&device=browser&"
                f"capabilities=D7F&clientType=VK&tgt=start"
            )

            headers = {
                "Upgrade": "websocket",
                "Origin": "https://web.vk.me",
                "Cache-Control": "no-cache",
                "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,ja;q=0.7",
                "Pragma": "no-cache",
                "Connection": "Upgrade",
                "Sec-WebSocket-Key": "BCIfkiM4N6ZsEYkwJ84VWw==",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7); AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                "Sec-WebSocket-Version": 13,
                "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            }
            message = ""
            with connect(url, additional_headers=headers) as ws:
                message = {"command": "hangup", "sequence": 20, "reason": "HUNGUP"}
                ws.send(json.dumps(message))
                message = ws.recv()
                ws.close()
            self.__conversation_id = None
            return PeerCallEnd(**json.loads(message))
        except websockets.exceptions.ConcurrencyError:
            raise RuntimeError(f"Request to {url} concurrency.")
        except websockets.exceptions.WebSocketException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")
