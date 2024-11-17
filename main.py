import SferumAPI

# Инициализация
remixdsid = "" # значение берется из cookies
api = SferumAPI.SferumAPI(remixdsid=remixdsid)

# Получение историй сообщений
messages_history = api.messages.get_history(peer_id=0, count=1, offset=0) # peer_id - id чата в Сферум
print(messages_history.response.items[0].text)

channel_history = api.channels.get_history(channel_id=-1, count=1, offset=0)
print(channel_history.response.items[0].attachments[0].wall.attachments[0].photo.sizes[0].url)

# Звонки
api.calls.peer.set_peer_id(peer_id=0) # peer_id - id пользователя в Сферум
api.calls.peer.start()
input()
api.calls.peer.end()

# Отправка сообщения
api.messages.send_message(peer_id=0, text="SferumAPI") # peer_id - id пользователя в Сферум