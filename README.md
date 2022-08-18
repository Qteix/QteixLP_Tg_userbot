# QteixLP Tg Version
## Установка
### Windows and Linux
```shell script
    git clone  https://github.com/Qteix/QteixLP_Tg_userbot.git
```

Переходим в папку и прописываем
```shell script
    python -r requirements.txt
```

Дальше заполняем `src/config.py`
В поле `api_id и api_hash` вводим вводим свои данные, которые мы получили отсюда https://my.telegram.org/apps
И запускаем скрипт
```shell script
    py -m src
```

## Список комманд
- `.пинг` Показывает информацию о ОС и время ответа в секундах.
- `.дем <reply_message_picture>` Делает демотиватор по отвеченному сообщению.
- `+гс <reply_message_voice> <name>` Добавляет голосовое сообщение с именем <name>.
- `-гс <name>` Удаляет голосовое сообщение с названием <name>.
- `.гс <name>` Отправляет голосовое сообщение с именем <name>.
- `.гсы` Показывает текущие сохраненные голосовые шаблоны.
