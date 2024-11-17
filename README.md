# SferumAPI

**SferumAPI** — это Python-библиотека, предоставляющая удобный интерфейс для работы с закрытым API Сферума. Она упрощает выполнение рутинных задач и позволяет легко интегрировать функционал Сферума в ваши проекты.

---

### Функционал

| **Функция**                           | **Статус** |
| ------------------------------------- | ---------- |
| 🔑 Авторизация пользователя в Сферуме | ✅         |
| 🔑 Авторизация сессии для звонков     | ✅         |
| ✉️ Отправка сообщений пользователю    | ✅         |
| 📥 Получение сообщений из чатов       | ✅         |
| 📥 Получение сообщений из каналов     | ✅         |
| 📞 Создание групповых звонков         | ✅         |
| 🔗 Подключение к групповым звонкам    | ❌         |
| 🛑 Завершение групповых звонков       | ✅         |
| 📞 Создание личных звонков            | ✅         |
| 🔗 Подключение к личным звонкам       | ❌         |
| 🛑 Завершение личных звонков          | ✅         |
| 📢 Отправка сообщений в каналы        | ❓         |

✅ — Реализовано  
❌ — В планах  
❓ — Под вопросом

---

### Зачем создана?

Каждую неделю приходится вручную выполнять норму по сообщениям и звонкам. Это рутинная и скучная задача, для которой не существовало готовых инструментов автоматизации. **SferumAPI** решает эту проблему, делая процесс быстрым и удобным.

---

### Установка

Установите библиотеку через pip:

```python
pip install SferumAPI
```

Или клонируйте репозиторий и установите её локально:

```bash
git clone https://github.com/l2700l/SferumAPI
cd SferumAPI
pip install .
```

---

### Пример использования

```python
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
```

---

### Обратная связь и вклад в развитие

Если у вас есть предложения по улучшению или вы нашли ошибку, создайте issue в репозитории. **Pull requests** приветствуются!

**Разработано с заботой о преподавателях и учителей ❤️**
