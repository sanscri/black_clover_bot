# Улучшенная версия кода для для Python 3.10+
async def send_message_user(bot, user_id, content_type, content_text=None, file_id=None, kb=None):
    match content_type:
        case 'text': await bot.send_message(chat_id=user_id, text=content_text, reply_markup=kb)
        case 'photo': await bot.send_photo(chat_id=user_id, photo=file_id, caption=content_text, reply_markup=kb)
        case 'document': await bot.send_document(chat_id=user_id, document=file_id, caption=content_text, reply_markup=kb)
        case 'video': await bot.send_video(chat_id=user_id, video=file_id, caption=content_text, reply_markup=kb)
        case 'audio': await bot.send_audio(chat_id=user_id, audio=file_id, caption=content_text, reply_markup=kb)
        case 'voice': await bot.send_voice(chat_id=user_id, voice=file_id, caption=content_text, reply_markup=kb)