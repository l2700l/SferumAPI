"""
Модуль работы с сообщениями

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from random import randint
import requests
from ..models import Message, MessagesHistory, UserCredentials, Response


class MessageService:
    """Сервис работы с сообщениями"""

    def __init__(self, user: UserCredentials):
        self.__user = user

    def send_message(
        self, peer_id: int, text: str, version: str = "5.223"
    ):
        """Отправка сообщения пользователю"""
        try:
            url = "https://api.vk.me/method/messages.send"
            data = {
                "access_token": self.__user.access_token,
                "peer_id": peer_id,
                "random_id": -randint(100000000, 999999999),
                "message": text,
            }
            params = {"v": version}
            response = requests.post(url, params=params, data=data, timeout=3)
            response.raise_for_status()
            return Response[Message](Message(**response.json()["response"]))
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")

    def get_history(self, peer_id: int, count: int, offset: int) -> MessagesHistory:
        """Получение истории сообщений"""
        try:
            url = "https://api.vk.me/method/messages.getHistory?v=5.241"

            data = {
                "access_token": self.__user.access_token,
                "peer_id": peer_id,
                "start_cmid": randint(1, 1000),
                "count": count,
                "offset": offset,
                "extended": "1",
                "group_id": "0",
                "fwd_extended": "1",
                "lang": "ru",
                "fields": "id,first_name,first_name_gen,first_name_acc,first_name_ins,last_name,last_name_gen,last_name_acc,last_name_ins,sex,has_photo,photo_id,photo_50,photo_100,photo_200,contact_name,occupation,bdate,city,screen_name,online_info,verified,blacklisted,blacklisted_by_me,can_call,can_write_private_message,can_send_friend_request,can_invite_to_chats,friend_status,followers_count,profile_type,contacts,employee_mark,employee_working_state,is_service_account,image_status,photo_base,educational_profile,edu_roles,name,type,members_count,member_status,is_closed,can_message,deactivated,activity,ban_info,is_messages_blocked,can_send_notify,can_post_donut,site,reposts_disabled,description,action_button,menu,role,unread_count,wall",
            }

            response = requests.post(url, data=data, timeout=3)
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")
