# Telegram bot for shop
## Change language: [English](README.en.md)
***
Телеграмм бот для предоставления информации о компании и приема заявок.
## [LIVE](https://t.me/outfit_item_bot)
## [DEMO](README.demo.md)
## Функционал:
1. Предоставляет информацию по различным аспектам деятельности компании
2. Содержит ссылки на социальные сети и контакты
3. Принимает заявки по сценарию, зависящему от ответов пользователей
4. Уведомляет менеджеров об оставленных заявках
5. Контролирует наличие имени пользователя в telegram
## Установка и использование:
- Установить зависимости:
```sh
pip install -r requirements.txt
```
- в файле .env указать:
  - Токен телеграмм бота: **TELEGRAM_TOKEN**=ТОКЕН
  - ID бота: **BOT_ID**=ID (первые цифры из токена бота, до :)
  - ID менеджера: **MANAGER_ID**=MANAGER_ID; будет иметь право на выполнение команды /update, ему будут приходить уведомления - для получения уведомлений менеджеру необходимо активировать бота со своего аккаунта (нажать кнопку "начать")
  > Для определения ID пользователя нужно отправить следующему [боту](https://t.me/getmyid_bot) любое сообщение с соответствующего аккаунта. Значение, содержащееся в **Your user ID** - ID пользователя
- в файле config.py задать следующие переменные:\
**MANAGER_USERNAME**=example (указывается без @) - ник менеджера\
**INSTAGRAM** - ссылка на instagram\
**WEB_URL** - ссылка на сайт\
**TELEGRAM_CHANNEL** - ссылка на telegram канал\
**WHATSAPP** - ссылка на профиль whatsapp\
**REVIEWS_IMAGE** - id изображения, отображающегося при переходе в раздел с отзывами, или ссылка на него\
**INSTRUCTION_IMAGE** - id изображения-инструкции или ссылка на него
- запустить проект:
```sh
python3 main.py
```
