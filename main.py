import telebot
import threading

import config
import text
import utils
import functions
import keyboards


bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    '''Handles start command.'''

    if not functions.is_in_database(message.from_user.id):
        functions.add_user(message.from_user.id, message.from_user.username)
    else:
        functions.drop_info(message.from_user.id)
    
    bot.send_message(chat_id=message.chat.id,
                         text=text.WELCOME_MESSAGE,
                         reply_markup=keyboards.reply_keyboard(),
                         parse_mode='Markdown',
                         disable_notification=True,
                         )
    
    bot.send_message(chat_id=message.chat.id,
                         text=text.MAIN_MENU,
                         reply_markup=keyboards.main_keyboard(),
                         parse_mode='Markdown',
                         disable_notification=True,
                         )
    
    
@bot.callback_query_handler(func = lambda call: True)
def callback_query(call):
    """Handles queries from inline keyboards."""

    # getting message's and user's ids
    message_id = call.message.id
    chat_id = call.message.chat.id
    username = call.from_user.username
    user_id = call.from_user.id

    call_data = call.data.split('_')
    query = call_data[0]

    if query == 'about':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.ABOUT_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.about_keyboard(),
                                      )
        
    elif query == 'manager':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.MANAGER_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.manager_back_keyboard(),
                                      )

    elif query == 'order':
        if username:
            functions.update_info(user_id, 'username', username)

            bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=text.BRAND_MESSAGE,
                                parse_mode='Markdown',
                                )
            
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.brands_keyboard(),
                                        )
        else:
            bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=text.NO_USERNAME,
                                parse_mode='Markdown',
                                )
            
            bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.username_keyboard(),
                                        )

    
    elif query == 'bonus':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.BONUS_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.back_main_keyboard(),
                                      )
    
    elif query == 'socials':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.SOCIAL_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.socials_back_keyboard(),
                                      )
        
    elif query == 'delivery':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.DELIVERY_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.back_about_keyboard(),
                                      )
    
    elif query == 'reviews':
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        bot.send_photo(chat_id=chat_id,
                       photo=config.REVIEWS_IMAGE,
                       caption=text.REVIEWS_MESSAGE,
                       reply_markup=keyboards.instagram_keyboard(),
                       parse_mode='Markdown',
                       )
    
    elif query == 'contacts':
        bot.edit_message_text(chat_id=chat_id,
                              message_id=message_id,
                              text=text.CONTACTS_MESSAGE,
                              parse_mode='Markdown',
                              )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=keyboards.contacts_keyboard(),
                                      )
    
    elif query == 'brand':
        brand = call_data[1]

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        if brand == 'another':
            functions.update_info(user_id, 'brand', None)
            functions.update_info(user_id, 'info_type', 'brand')

            bot.send_message(chat_id=chat_id,
                             text=text.BRAND_QUESTION,
                             reply_markup=keyboards.back_brand_keyboard(),
                             )
        else:
            functions.update_info(user_id, 'brand', brand)
            functions.update_info(user_id, 'info_type', 'photo')

            bot.send_message(chat_id=chat_id,
                             text=text.photo_question(brand),
                             reply_markup= keyboards.back_brand_keyboard(),
                             parse_mode='Markdown',
                             )
            
    elif query == 'size':
        answer = call_data[1]

        if answer == 'yes':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.METRICS_MESSAGE,
                                  parse_mode='Markdown',
                                  )
            
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.metrics_keyboard(),
                                          )
        if answer == 'no':
            try:
                bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass
            
            functions.update_info(user_id, 'metric', 'cm')
            functions.update_info(user_id, 'info_type', 'size')

            bot.send_photo(chat_id=chat_id,
                           photo=config.INSTRUCTION_IMAGE,
                           caption=text.SIZE_QUESTION,
                           reply_markup=keyboards.back_size_keyboard(),
                           parse_mode='Markdown',
                           )

    elif query == 'metrics':
        metric = call_data[1]

        functions.update_info(user_id, 'metric', metric)
        functions.update_info(user_id, 'info_type', 'size')

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        bot.send_message(chat_id=chat_id,
                         text=text.size_metric_question(metric),
                         reply_markup=keyboards.back_metric_keyboard(),
                         parse_mode='Markdown',
                         )
        
    elif query == 'menu':
        functions.drop_info(user_id)

        bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.MAIN_MENU,
                                  parse_mode='Markdown',
                                  )
            
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.main_keyboard(),
                                        )

    elif query == 'refill':
        functions.drop_info(user_id)

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        
        if username:
            functions.update_info(user_id, 'username', username)

            bot.send_message(chat_id=chat_id,
                                text=text.BRAND_MESSAGE,
                                reply_markup=keyboards.brands_keyboard(),
                                parse_mode='Markdown',
                                )

        else:
            bot.send_message(chat_id=chat_id,
                                text=text.NO_USERNAME,
                                reply_markup=keyboards.username_keyboard(),
                                parse_mode='Markdown',
                                )
    
    elif query == 'cancel':
        functions.drop_info(user_id)

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        bot.send_message(chat_id=chat_id,
                         text=text.CANCELED,
                         reply_markup=keyboards.menu_keyboard(),
                         )
    
    elif query == 'confirm':
        order_info = functions.select_order(user_id)

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        if order_info[8] == str(message_id):
            threading.Thread(daemon=True, target=functions.inform_manager, args=(order_info,)).start()

            bot.send_message(chat_id=chat_id,
                            text=text.END_MESSAGE,
                            reply_markup=keyboards.socials_keyboard(),
                            parse_mode='Markdown',
                            )
        else:
            bot.send_message(chat_id=chat_id,
                         text=text.OUTDATED,
                         reply_markup=keyboards.menu_keyboard(),
                         )
            
    elif query == 'back':
        destination = call_data[1]

        if destination == 'main':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.MAIN_MENU,
                                  parse_mode='Markdown',
                                  )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.main_keyboard(),
                                          )
            
        elif destination == 'about':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.ABOUT_MESSAGE,
                                  parse_mode='Markdown',
                                  )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.about_keyboard(),
                                          )
        
        elif destination == 'deleteabout':
            try:
                bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass

            bot.send_message(chat_id=chat_id,
                             text=text.ABOUT_MESSAGE,
                             reply_markup=keyboards.about_keyboard(),
                             parse_mode='Markdown',
                             )
        
        elif destination == 'size':
            functions.update_info(user_id, 'info_type', None)

            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.SIZE_MESSAGE,
                                  parse_mode='Markdown',
                                  )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.size_keyboard(),
                                          )
        
        elif destination == 'brand':
            brand = functions.select_brand(user_id)

            if brand in config.BRANDS or brand is None:
                functions.update_info(user_id, 'info_type', None)

                bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=text.BRAND_MESSAGE,
                                    parse_mode='Markdown',
                                    )
            
                bot.edit_message_reply_markup(chat_id=chat_id,
                                            message_id=message_id,
                                            reply_markup=keyboards.brands_keyboard(),
                                            )
            else:
                functions.update_info(user_id, 'info_type', 'brand')
                functions.update_info(user_id, 'brand', None)
                                      
                bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=text.BRAND_QUESTION,
                                    parse_mode='Markdown',
                                    )
            
                bot.edit_message_reply_markup(chat_id=chat_id,
                                            message_id=message_id,
                                            reply_markup=keyboards.back_brand_keyboard(),
                                            )
        
        elif destination == 'photo':
            
            functions.update_info(user_id, 'info_type', 'photo')

            brand = functions.select_brand(user_id)
            if brand in config.BRANDS:
                reply_text = text.photo_question(brand)
            else:
                reply_text = text.photo_question_alt(brand)

            try:
                bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=reply_text,
                                    parse_mode='Markdown',
                                    )
            except:
                reply_text = reply_text.replace('*', '')

                bot.edit_message_text(chat_id=chat_id,
                                    message_id=message_id,
                                    text=reply_text,
                                    )

            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.back_brand_keyboard(),
                                          )

        elif destination == 'deletesize':
            functions.update_info(user_id, 'info_type', None)

            try:
                bot.delete_message(chat_id=chat_id, message_id=message_id)
            except:
                pass

            bot.send_message(chat_id=chat_id,
                             text=text.SIZE_MESSAGE,
                             reply_markup=keyboards.size_keyboard(),
                             parse_mode='Markdown',
                             )
            
        elif destination == 'metric':
            functions.update_info(user_id, 'info_type', None)

            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=text.METRICS_MESSAGE,
                                  parse_mode='Markdown',
                                  )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.metrics_keyboard(),
                                          )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Handles message with type text."""
    
    user_id = message.from_user.id
    chat_id = message.chat.id

    if message.text == '📱 Меню':
        functions.drop_info(user_id)

        bot.send_message(chat_id=chat_id,
                         text=text.MAIN_MENU,
                         reply_markup=keyboards.main_keyboard(),
                         parse_mode='Markdown',
                         disable_notification=True,
                         )
        
    elif message.text == '👨‍💻 Менеджер':
        bot.send_message(chat_id=chat_id,
                         text=text.MANAGER_MESSAGE,
                         reply_markup=keyboards.manager_keyboard(),
                         parse_mode='Markdown',
                         disable_notification=True,
                         )
    
    else:
        info_type = functions.check_info_type(user_id)

        if info_type:
            if info_type == 'brand':
                functions.update_info(user_id, 'brand', message.text)
                functions.update_info(user_id, 'info_type', 'photo')

                try:
                    bot.send_message(chat_id=chat_id,
                                text=text.photo_question_alt(message.text),
                                reply_markup = keyboards.back_brand_keyboard(),
                                parse_mode='Markdown',
                                )
                except:
                    try:
                        bot.send_message(chat_id=chat_id,
                                text=text.photo_question_alt(message.text).replace('*', ''),
                                reply_markup = keyboards.back_brand_keyboard(),
                                )
                    except:
                        pass
                
            elif info_type == 'size':
                size = utils.validate_size(message.text)

                if size:
                    functions.update_info(user_id, 'size', size)
                    functions.update_info(user_id, 'info_type', None)

                    order_info = functions.select_order(user_id)
                    reply_text = text.order_info(order_info)
                    try:
                        sended_message = bot.send_photo(chat_id=chat_id,
                                    photo=order_info[5],
                                    caption=reply_text,
                                    reply_markup=keyboards.confirm_keyboard(),
                                    parse_mode='Markdown',
                                    )
                    except:
                        reply_text = reply_text.replace('*', '')

                        sended_message = bot.send_photo(chat_id=chat_id,
                                    photo=order_info[5],
                                    caption=reply_text,
                                    reply_markup=keyboards.confirm_keyboard(),
                                    )
                        
                    functions.update_info(user_id, 'message_id', sended_message.id)
                    
                else:
                    bot.send_message(chat_id=chat_id,
                                    text=text.SIZE_FORMAT,
                                    )

        else:
            bot.send_message(chat_id=chat_id,
                             text=text.NO_INFO_TYPE,
                             reply_markup=keyboards.menu_keyboard(),
                             parse_mode='Markdown'
                             )


@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    info_type = functions.check_info_type(user_id)

    if info_type == 'photo':
        bot.send_message(chat_id=chat_id,
                         text=text.NOT_DOCUMENT,
                         )


@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    user_id = message.from_user.id
    chat_id = message.chat.id
    info_type = functions.check_info_type(user_id)

    if info_type == 'photo':
        functions.update_info(user_id, 'photo', message.photo[1].file_id)
        functions.update_info(user_id, 'info_type', None)

        bot.send_message(chat_id=chat_id,
                         text=text.SIZE_MESSAGE,
                         reply_markup=keyboards.size_keyboard(),
                         )
    
    else:
        bot.send_message(chat_id=chat_id,
                         text=text.NO_PHOTO_TYPE,
                         reply_markup=keyboards.menu_keyboard(),
                         parse_mode='Markdown',
                         )


if __name__ == '__main__':
    # bot.polling(timeout=80)
    while True:
        try:
            bot.polling()
        except:
            pass