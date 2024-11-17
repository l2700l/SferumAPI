"""
Модуль работы с сообществами

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from random import randint
import requests
from ..models import UserCredentials, ChannelHistory


class ChannelService:
    """Сервис работы с каналами"""

    def __init__(self, user: UserCredentials):
        self.__user = user

    def get_history(self, channel_id: int, count: int, offset: int) -> ChannelHistory:
        """Получение истории сообщений"""
        try:
            url = "https://api.vk.me/method/channels.getHistory?v=5.241"

            data = {
                "access_token": self.__user.access_token,
                "channel_id": channel_id,
                "start_cmid": randint(1, 1000),
                "count": count,
                "offset": offset,
                "extended": "1",
                "lang": "ru",
                "fields": "id,first_name,first_name_gen,first_name_acc,first_name_ins,last_name,last_name_gen,last_name_acc,last_name_ins,sex,has_photo,photo_id,photo_50,photo_100,photo_200,contact_name,occupation,bdate,city,screen_name,online_info,verified,blacklisted,blacklisted_by_me,can_call,can_write_private_message,can_send_friend_request,can_invite_to_chats,friend_status,followers_count,profile_type,contacts,employee_mark,employee_working_state,is_service_account,image_status,photo_base,educational_profile,edu_roles,name,type,members_count,member_status,is_closed,can_message,deactivated,activity,ban_info,is_messages_blocked,can_send_notify,can_post_donut,site,reposts_disabled,description,action_button,menu,role,unread_count,wall",
            }

            response = requests.post(url, data=data, timeout=3)
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"An error occurred during the request to {url}: {e}")
