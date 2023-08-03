import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOT_ID = os.getenv('BOT_ID')
MANAGER_ID = os.getenv('MANAGER_ID')

MANAGER_USERNAME = 'outfit_item'
INSTAGRAM = 'https://www.instagram.com/outfit.item/'
WEB_URL = 'https://outfit-item.ru'
TELEGRAM_CHANNEL = 'https://t.me/outfititem'
WHATSAPP = 'https://wa.me/79936009525'

REVIEWS_IMAGE = 'AgACAgIAAxkBAAMGZMtrNZhgc5lc6ehiWQtvf_TfpvAAAknKMRtcxFhKrTUDlBk6l0gBAAMCAAN5AAMvBA'
INSTRUCTION_IMAGE = 'AgACAgIAAxkBAAMIZMtrSdHLHmGA1yXPoNiXqoH9NRcAAk_KMRtcxFhKbrqaCSL4j4IBAAMCAAN4AAMvBA'

METRICS = {
    'ru' : 'RU - Россия',
    'eu' : 'EU - Европа',
    'us' : 'US - Америка',
    'uk' : 'UK - Англия',
    'cm' : 'CM - сантиметры',
}


BRANDS = ['Adidas', 'Nike', 'New Balance', 'Converse']
