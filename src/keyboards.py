from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton
                           )


reply_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Каталог"), KeyboardButton(text="Контакты")]
], resize_keyboard=True, input_field_placeholder="Выберите пункт")


inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
    [InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")]
])

inline_buttons2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать занова', callback_data='restart_start')]
])

update_delete_button_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Удалить', callback_data='delete_user')],
    [InlineKeyboardButton(text='Изменить', callback_data='update_user')]
])