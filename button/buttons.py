from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
main_btn = ReplyKeyboardMarkup(resize_keyboard=True)
main_btn.add('🕠 Ramazon taqvimi', '®️ Viloyatlar')
main_btn.add('➡️ Boshqa bo`limlar', '🆘 Yordam markazi')


ramazon_btn = ReplyKeyboardMarkup(resize_keyboard=True)
ramazon_btn.add('📿 Bugungi kun', '📿 Ertangi kun')
ramazon_btn.add('🗓 Oylik taqvim', '🔙 Orqaga')

async def provinces():
    Markup = InlineKeyboardMarkup(row_width=2)
    Markup.add(InlineKeyboardButton(text='Toshkent', callback_data='Toshkent'))
    Markup.insert(InlineKeyboardButton(text='Andijon', callback_data='Andijon'))
    Markup.insert(InlineKeyboardButton(text='Buxoro', callback_data='Buxoro'))
    Markup.insert(InlineKeyboardButton(text='Guliston', callback_data='Guliston'))
    Markup.insert(InlineKeyboardButton(text='Samarqand', callback_data='Samarqand'))
    Markup.insert(InlineKeyboardButton(text='Namangan', callback_data='Namangan'))
    Markup.insert(InlineKeyboardButton(text='Navoiy', callback_data='Navoiy'))
    Markup.insert(InlineKeyboardButton(text='Jizzax', callback_data='Jizzax'))
    Markup.insert(InlineKeyboardButton(text='Nukus', callback_data='Nukus'))
    Markup.insert(InlineKeyboardButton(text='Qarshi', callback_data='Qarshi'))
    Markup.insert(InlineKeyboardButton(text='Qoqon', callback_data='Qoqon'))
    Markup.insert(InlineKeyboardButton(text='Xiva', callback_data='Xiva'))
    Markup.insert(InlineKeyboardButton(text='Margilon', callback_data='Margilon'))
    return Markup