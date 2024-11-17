"""
calls models

:copyright: (c) 2024 by l2700l.
:license: MIT, see LICENSE for more details.
:author: l2700l <thetypgame@gmail.com>
"""

import dataclasses


@dataclasses.dataclass
class TurnServer:
    urls: list[str]
    username: str
    credential: str


@dataclasses.dataclass
class StunServer:
    urls: list[str]


@dataclasses.dataclass
class CallStart:
    token: str
    endpoint: str
    turn_server: TurnServer
    stun_server: StunServer
    client_type: str
    device_idx: int
    id: str
    join_link: str
    is_concurrent: bool
    p2p_forbidden: bool

    def __init__(self, **kwargs) -> None:
        self.token = kwargs.get("token")
        self.endpoint = kwargs.get("endpoint")
        self.turn_server = TurnServer(**kwargs.get("turn_server", {}))
        self.stun_server = StunServer(**kwargs.get("stun_server", {}))
        self.client_type = kwargs.get("client_type")
        self.device_idx = kwargs.get("device_idx", 0)
        self.id = kwargs.get("id")
        self.join_link = kwargs.get("join_link")
        self.is_concurrent = kwargs.get("is_concurrent", False)
        self.p2p_forbidden = kwargs.get("p2p_forbidden", False)


@dataclasses.dataclass
class ExternalId:
    type: str
    id: str


@dataclasses.dataclass
class MediaSettings:
    is_audio_enabled: bool

    def __init__(self, **kwargs):
        self.is_audio_enabled = kwargs.get("isAudioEnabled")


@dataclasses.dataclass
class PeerId:
    id: int


@dataclasses.dataclass
class Participant:
    external_id: ExternalId
    state: str
    roles: list[str]
    media_settings: MediaSettings
    peer_id: PeerId
    responders: list[int]
    responder_types: list[str]
    responder_device_idxs: list[int]
    permissions: list[str]
    id: int

    def __init__(self, **kwargs) -> None:
        self.external_id = ExternalId(**kwargs.get("externalId", {}))
        self.state = kwargs.get("state")
        self.roles = kwargs.get("roles", [])
        self.media_settings = MediaSettings(**kwargs.get("mediaSettings", {}))
        self.peer_id = PeerId(**kwargs.get("peerId", {"id": 0}))
        self.responders = kwargs.get("responders", [])
        self.responder_types = kwargs.get("responderTypes", [])
        self.responder_device_idxs = kwargs.get("responderDeviceIdxs", [])
        self.permissions = kwargs.get("permissions", [])
        self.id = kwargs.get("id")


@dataclasses.dataclass
class Conversation:
    id: str
    state: str
    topology: str
    participants: list[Participant]
    participants_limit: int
    features: list[str]
    features_per_role: dict
    turn_servers: list[str]
    join_link: str
    options: list[str]
    client_type: str
    hand_count: int

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.state = kwargs.get("state")
        self.topology = kwargs.get("topology")
        self.participants = [Participant(**p) for p in kwargs.get("participants", [])]
        self.participants_limit = kwargs.get("participantsLimit", 0)
        self.features = kwargs.get("features", [])
        self.features_per_role = kwargs.get("featuresPerRole", {})
        self.turn_servers = kwargs.get("turnServers", [])
        self.join_link = kwargs.get("joinLink")
        self.options = kwargs.get("options", [])
        self.client_type = kwargs.get("clientType")
        self.hand_count = kwargs.get("handCount", 0)


@dataclasses.dataclass
class ConversationParams:
    server_time: int
    activity_timeout: int

    def __init__(self, **kwargs):
        self.server_time = kwargs.get("serverTime")
        self.activity_timeout = kwargs.get("activityTimeout")


@dataclasses.dataclass
class MediaModifiers:
    denoise: bool
    denoise_ann: bool

    def __init__(self, **kwargs):
        self.denoise = kwargs.get("denoise")
        self.denoise_ann = kwargs.get("denoiseAnn")


@dataclasses.dataclass
class PeerCallEnd:
    stamp: int
    peer_id: PeerId
    endpoint: str
    conversation_params: ConversationParams
    conversation: Conversation
    is_concurrent: bool
    media_modifiers: MediaModifiers
    notification: str
    type: str

    def __init__(self, **kwargs) -> None:
        self.stamp = kwargs.get("stamp")
        self.peer_id = PeerId(**kwargs.get("peerId", {}))
        self.endpoint = kwargs.get("endpoint")
        self.conversation_params = ConversationParams(
            **kwargs.get("conversationParams", {})
        )
        self.conversation = Conversation(**kwargs.get("conversation", {}))
        self.is_concurrent = kwargs.get("isConcurrent", False)
        self.media_modifiers = MediaModifiers(**kwargs.get("mediaModifiers", {}))
        self.notification = kwargs.get("notification")
        self.type = kwargs.get("type")
