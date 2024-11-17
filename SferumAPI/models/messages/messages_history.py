"""
messages models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from dataclasses import dataclass
from json_to_models.dynamic_typing import IntString
from typing import Any, List, Optional


@dataclass
class MessagesHistory:
    response: "Response"


@dataclass
class Response:
    count: int
    items: List["Item"]
    profiles: List["Profile"]
    conversations: List["Conversation"]


@dataclass
class Item:
    date_: int
    from_id: int
    id_: int
    version: int
    out: int
    important: bool
    is_hidden: bool
    reactions: List["Reaction"]
    last_reaction_id: int
    attachments: List[Any]
    conversation_message_id: int
    fwd_messages: List[Any]
    text: str
    is_mentioned_user: bool
    peer_id: int
    random_id: int


@dataclass
class Reaction:
    reaction_id: int
    count: int
    user_ids: List[int]


@dataclass
class Profile:
    id_: int
    first_name_gen: str
    first_name_acc: str
    first_name_ins: str
    last_name_gen: str
    last_name_acc: str
    last_name_ins: str
    bdate: str
    photo_200: str
    has_photo: int
    can_call: bool
    can_write_private_message: int
    can_send_friend_request: int
    site: str
    activity: str
    followers_count: int
    blacklisted: int
    blacklisted_by_me: int
    can_invite_to_chats: bool
    is_service_account: bool
    educational_profile: "EducationalProfile"
    sex: int
    screen_name: str
    photo_50: str
    photo_100: str
    photo_base: str
    online_info: "OnlineInfo"
    verified: int
    friend_status: int
    first_name: str
    last_name: str
    can_access_closed: bool
    is_closed: bool
    photo_id: Optional[IntString] = None
    mobile_phone: Optional[str] = None
    home_phone: Optional[str] = None


@dataclass
class EducationalProfile:
    edu_roles: "EduRole"


@dataclass
class EduRole:
    user_id: int
    main_roles: str
    main_role_code: str
    organizations: List["Organization"]


@dataclass
class Organization:
    organization_id: int
    organization_type: IntString
    organization_name: str
    roles: List["Role"]


@dataclass
class Role:
    role_code: str
    details: str
    order: int


@dataclass
class OnlineInfo:
    visible: bool
    status: str


@dataclass
class Conversation:
    peer: "Peer"
    last_message_id: int
    last_conversation_message_id: int
    in_read: int
    out_read: int
    in_read_cmid: int
    out_read_cmid: int
    version: int
    sort_id: "SortId"
    is_marked_unread: bool
    important: bool
    can_write: "CanWrite"
    can_send_money: bool
    can_receive_money: bool
    chat_settings: "ChatSetting"
    peer_flags: int


@dataclass
class Peer:
    id_: int
    type_: str
    local_id: int


@dataclass
class SortId:
    major_id: int
    minor_id: int


@dataclass
class CanWrite:
    allowed: bool


@dataclass
class ChatSetting:
    title: str
    members_count: int
    owner_id: int
    description: str
    pinned_messages_count: int
    state: str
    is_group_channel: bool
    acl: "Acl"
    is_disappearing: bool
    is_service: bool
    type_mask: int
    is_incognito: bool


@dataclass
class Acl:
    can_change_info: bool
    can_change_invite_link: bool
    can_change_pin: bool
    can_invite: bool
    can_promote_users: bool
    can_see_invite_link: bool
    can_moderate: bool
    can_copy_chat: bool
    can_call: bool
    can_use_mass_mentions: bool
    can_change_style: bool
    can_send_reactions: bool
