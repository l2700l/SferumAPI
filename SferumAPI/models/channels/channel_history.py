"""
channels models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ChannelHistory:
    response: "Response"


@dataclass
class Response:
    count: int
    items: List["Item"]
    profiles: List["Profile"]
    groups: List["Group"]


@dataclass
class Item:
    channel_id: int
    cmid: int
    author_id: int
    time_: int
    attachments: List["Attachment"]


@dataclass
class Attachment:
    type_: str
    wall: "Wall"


@dataclass
class Wall:
    inner_type: str
    donut: "Donut"
    comments: "Comment"
    marked_as_ads: int
    type_: str
    to_id: int
    carousel_offset: int
    access_key: str
    attachments: List["Attachment_1H"]
    date_: int
    from_id: int
    id_: int
    is_favorite: bool
    likes: "Like"
    reaction_set_id: str
    reactions: "Reaction"
    owner_id: int
    post_source: "PostSource"
    post_type: str
    reposts: "Repost"
    text: str
    views: "View"
    track_code: str


@dataclass
class Donut:
    is_donut: bool


@dataclass
class Comment:
    can_post: int
    can_view: int
    count: int
    groups_can_post: bool


@dataclass
class Attachment_1H:
    type_: str
    photo: "Photo"


@dataclass
class Photo:
    album_id: int
    date_: int
    id_: int
    owner_id: int
    access_key: str
    sizes: List["OrigPhoto_Size"]
    text: str
    user_id: int
    web_view_token: str
    has_tags: bool
    orig_photo: "OrigPhoto_Size"


@dataclass
class Like:
    can_like: int
    count: int
    user_likes: int
    can_publish: int
    repost_disabled: bool


@dataclass
class Reaction:
    count: int
    items: List["Item_1N"]


@dataclass
class OrigPhoto_Size:
    height: int
    type_: str
    url: str
    width: int


@dataclass
class Item_1N:
    id_: int
    count: int


@dataclass
class PostSource:
    type_: str


@dataclass
class Repost:
    count: int
    user_reposted: int


@dataclass
class View:
    count: int


@dataclass
class Profile:
    id_: int
    first_name_gen: str
    first_name_acc: str
    first_name_ins: str
    last_name_gen: str
    last_name_acc: str
    last_name_ins: str
    photo_200: str
    has_photo: int
    can_write_private_message: int
    site: str
    blacklisted_by_me: int
    is_service_account: bool
    sex: int
    screen_name: str
    photo_50: str
    photo_100: str
    photo_base: str
    online_info: "OnlineInfo"
    friend_status: int
    deactivated: str
    first_name: str
    last_name: str
    can_access_closed: bool
    is_closed: bool


@dataclass
class OnlineInfo:
    visible: bool
    is_online: bool
    is_mobile: bool


@dataclass
class Group:
    id_: int
    member_status: int
    description: str
    members_count: int
    activity: str
    has_photo: int
    contacts: List["Contact"]
    wall: int
    site: str
    can_message: int
    is_messages_blocked: int
    reposts_disabled: bool
    name: str
    screen_name: str
    is_closed: int
    type_: str
    is_admin: int
    is_member: int
    is_advertiser: int
    verified: int
    photo_50: str
    photo_100: str
    photo_200: str
    photo_base: str


@dataclass
class Contact:
    user_id: int
