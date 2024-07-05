# Aiogram_voice_bot
Уведомление о появлении новых заказов на фриланс-бирже Kwork

## Функционал
- Голосовое управление;
- Интервальный парсинг;
- Уведомление о появлении новых заказов;

## Стэк
- Для конвертации голосовых сообщений телеграма в формате .ogg в формат .wav - был выбран ffmpeg
- Для перевода речи в текс - speach_recognition
- python==3.7.2

## Установка
```sh
python -m venv venv
venv\Scripts\activate
pip install -r .\requirements.txt
python manage.py app.py
```
Нужно установить ffmpeg, используя эту [инструкцию](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
Также, необходимо создать файл .env и добавить туда переменную TOKEN=<token>, сам токен можно получить у @BotFather

## ВАЖНО!
Бот больше не работает, т.к Kwork поменяли структуру данных и парсер необходимо доработать, либо вовсе заменить
