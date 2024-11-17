"""
Модуль работы с пользователями

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import requests
from .auth_strategy import AuthStrategy
from ..models import UserCredentials


class UserAuth(AuthStrategy):
    """Реализация авторизации пользователя"""

    def __init__(self, remixdsid: str):
        super().__init__()
        self.remixdsid = remixdsid

    def authorize(self):
        try:
            cookies = {"remixdsid": self.remixdsid}
            query = {"act": "web_token", "app_id": 8202606}

            response = requests.get(
                "https://web.vk.me/",
                params=query,
                cookies=cookies,
                allow_redirects=False,
                timeout=3,
            )
            response.raise_for_status()
            return UserCredentials(**response.json()[1])
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to user authorize timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(
                f"An error occurred during the request to user authorize: {e}"
            )
