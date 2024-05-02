import traceback

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from StringGenBot.generate import generate_session, ask_ques, buttons_ques


@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram1|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("◍ ستكون الجلسة التي تم إنشاؤها من بايروجرام v2", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "◍ حدث خطأ ما \n\n**الخـطـأ** : {} " \
            "\n\n**◍ يرجى إعادة توجيه هذه الرسالة إلى @COUDRA_1**, إذا كانت هذه الرسالة " \
            "◍ لا تحتوي على أي معلومات خاصة" \
            "◍ لأن هذا الخطأ **لم تقم بتسجيل الدخول إلى الروبوت** !"