import sqlite3
import telebot

import config


bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


def is_in_database(user_id):
    """Checks if user already in database."""

    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    users = cursor.execute(f'''SELECT COUNT(id) 
                            FROM users 
                            WHERE user_id=?
                            ''', (user_id,)).fetchall()[0][0]
    
    cursor.close()
    database.close()

    return users


def add_user(user_id, username):
    """Adds a new user to database."""

    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    cursor.execute(f'''
        INSERT INTO users (user_id, username)
        VALUES (?, ?)
        ''', (user_id, username,))
        
    database.commit()
    cursor.close()
    database.close()


def update_info(user_id, field, value):
    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    cursor.execute(f'''UPDATE users
                    SET {field}=?
                    WHERE user_id=?
                    ''', (value, user_id,))

    database.commit()
    cursor.close()
    database.close()


def check_info_type(user_id):
    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    info_type = cursor.execute(f'''SELECT info_type 
                    FROM users
                    WHERE user_id=?
                    ''', (user_id,)).fetchall()[0][0]
    
    cursor.close()
    database.close()

    return info_type


def select_order(user_id):
    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    order_info = cursor.execute(f'''SELECT * 
                    FROM users
                    WHERE user_id=?
                    ''', (user_id,)).fetchall()[0]
    
    cursor.close()
    database.close()

    return order_info


def select_brand(user_id):
    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    order_info = cursor.execute(f'''SELECT brand 
                    FROM users
                    WHERE user_id=?
                    ''', (user_id,)).fetchall()[0][0]
    
    cursor.close()
    database.close()

    return order_info


def drop_info(user_id):
    database = sqlite3.connect("db.db")
    cursor = database.cursor()

    cursor.execute(f'''UPDATE users
                    SET info_type=?, brand=?, photo=?, metric=?, size=?, message_id=?
                    WHERE user_id=?
                    ''', (None, None, None, None, None, None, user_id,))

    database.commit()
    cursor.close()
    database.close()


def inform_manager(order_info):
    username = order_info[2]
    brand = order_info[4]
    photo = order_info[5]
    metric = config.METRICS[order_info[6]]
    size = order_info[7]

    text = f'''
            \nПользователь @{username} оставил заявку:\
            \n\
            \n*Бренд:* {brand}\
            \n*Метрика:* {metric}\
            \n*Размер:* {size}\
            '''
    
    try:
        bot.send_photo(chat_id=config.MANAGER_ID,
                       photo=photo,
                       caption=text,
                       parse_mode='Markdown',
                       )
    except:
        text = text.replace('*', '')

        try:
            bot.send_photo(chat_id=config.MANAGER_ID,
                       photo=photo,
                       caption=text,
                       )
        except:
            pass