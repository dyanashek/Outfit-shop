from telebot import types

import config


# inline клавиатура
def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    about = types.InlineKeyboardButton('О нас', callback_data = 'about')
    manager = types.InlineKeyboardButton('Менеджер', callback_data = 'manager')

    keyboard.add(about, manager)
    keyboard.add(types.InlineKeyboardButton('Индивидуальный заказ', callback_data = 'order'))
    keyboard.add(types.InlineKeyboardButton('🎁 Бонус', callback_data = 'bonus'))

    return keyboard


def about_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Социальные сети', callback_data = 'socials'))
    keyboard.add(types.InlineKeyboardButton('Варианты доставки', callback_data = 'delivery'))
    keyboard.add(types.InlineKeyboardButton('Отзывы', callback_data = 'reviews'))
    keyboard.add(types.InlineKeyboardButton('Контакты', callback_data = 'contacts'))
    keyboard.add(types.InlineKeyboardButton('Наш сайт', url = config.WEB_URL))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))

    return keyboard


def back_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))

    return keyboard


def back_about_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_about'))

    return keyboard

def back_brand_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_brand'))

    return keyboard

def back_photo_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_photo'))

    return keyboard

def back_size_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_deletesize'))

    return keyboard

def back_metric_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_metric'))

    return keyboard

def brands_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Adidas', callback_data = 'brand_Adidas'))
    keyboard.add(types.InlineKeyboardButton('Nike', callback_data = 'brand_Nike'))
    keyboard.add(types.InlineKeyboardButton('New Balance', callback_data = 'brand_New Balance'))
    keyboard.add(types.InlineKeyboardButton('Converse', callback_data = 'brand_Converse'))
    keyboard.add(types.InlineKeyboardButton('Другой бренд', callback_data = 'brand_another'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))

    return keyboard


def manager_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Чат с менеджером', url = f'https://t.me/{config.MANAGER_USERNAME}'))

    return keyboard


def manager_back_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Чат с менеджером', url = f'https://t.me/{config.MANAGER_USERNAME}'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))

    return keyboard


def size_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Да', callback_data = 'size_yes'), types.InlineKeyboardButton('Нет', callback_data = 'size_no'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_photo'))

    return keyboard


def metrics_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('RU - Россия', callback_data = 'metrics_ru'))
    keyboard.add(types.InlineKeyboardButton('EU - Европа', callback_data = 'metrics_eu'))
    keyboard.add(types.InlineKeyboardButton('US - Америка', callback_data = 'metrics_us'))
    keyboard.add(types.InlineKeyboardButton('UK - Англия', callback_data = 'metrics_uk'))
    keyboard.add(types.InlineKeyboardButton('CM - сантиметры', callback_data = 'metrics_cm'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_size'))

    return keyboard


def socials_back_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Instagram', url = config.INSTAGRAM))
    keyboard.add(types.InlineKeyboardButton('Telegram-канал', url = config.TELEGRAM_CHANNEL))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_about'))

    return keyboard


def socials_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Instagram', url = config.INSTAGRAM))
    keyboard.add(types.InlineKeyboardButton('Telegram-канал', url = config.TELEGRAM_CHANNEL))
    keyboard.add(types.InlineKeyboardButton('Чат с менеджером', url = f'https://t.me/{config.MANAGER_USERNAME}'))

    return keyboard


def instagram_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Instagram', url = config.INSTAGRAM))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_deleteabout'))

    return keyboard


def contacts_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('WhatsApp', url = config.WHATSAPP))
    keyboard.add(types.InlineKeyboardButton('Telegram', url = f'https://t.me/{config.MANAGER_USERNAME}'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = f'back_about'))

    return keyboard


def confirm_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('✅ Подтвердить', callback_data = 'confirm'))
    keyboard.add(types.InlineKeyboardButton('🔁 Заполнить заново', callback_data = 'refill'))
    keyboard.add(types.InlineKeyboardButton('❌ Отменить', callback_data = 'cancel'))

    return keyboard


def username_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('Индивидуальный заказ', callback_data = 'order'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = 'back_main'))

    return keyboard


def menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton('📱 Меню', callback_data = 'menu'))

    return keyboard


# reply клавиатура
def reply_keyboard():
    """Keyboard that allows ask for a call."""

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('📱 Меню'), types.KeyboardButton('👨‍💻 Менеджер'))

    return keyboard