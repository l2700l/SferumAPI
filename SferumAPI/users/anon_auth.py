"""
Модуль работы с пользователями

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import uuid
import requests
from .auth_strategy import AuthStrategy
from ..models import AnonCredentials


class AnonAuth(AuthStrategy):
    """Реализация авторизации сессии для звонков"""

    def __init__(self, access_token: str):
        super().__init__()
        self.device_id = str(uuid.uuid4())
        self.auth_token = self.__get_calls_token(access_token=access_token)

    def __get_calls_token(self, access_token: str) -> str:
        url = "https://api.vk.me/method/messages.getCallToken?v=5.241"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0",
        }
        data = {"access_token": access_token, "env": "production"}
        response = requests.post(url, headers=headers, data=data, timeout=3)
        response.raise_for_status()
        return response.json()["response"]["token"]

    def authorize(self):
        try:
            url = "https://api.mycdn.me/fb.do"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0",
            }
            data = {
                "session_data": f'{{"version":3,"device_id":"{self.device_id}","client_version":1.1,"client_type":"SDK_JS","auth_token":"{self.auth_token}"}}',
                "method": "auth.anonymLogin",
                "format": "JSON",
                "application_key": "CFJCCIJGDIHBABABA",
            }
            response = requests.post(url, headers=headers, data=data, timeout=3)
            response.raise_for_status()
            return AnonCredentials(**response.json())
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to anon authorize timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                f"An error occurred during the request to anon authorize: {e}"
            )
