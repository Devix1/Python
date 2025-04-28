from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Получить планы 🗒️')],
                                     [KeyboardButton(text='Наш телеграмм канал ✉️')]],
                                     one_time_keyboard=True,
                                     resize_keyboard=True,
                                     input_field_placeholder='Выбирите пункт меню...')

plans = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Тренировочный план 🏋️', callback_data='trainingPlan'),
                                                InlineKeyboardButton(text='План питания 🍎', callback_data='foodPlan')]])





floor = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Мужской 🧔‍♂️', callback_data='men1')],
                                              [InlineKeyboardButton(text='Женский 👩‍🦰', callback_data='woman1')]])

floor1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Мужской 🧔‍♂️', callback_data='men1.1')],
                                              [InlineKeyboardButton(text='Женский 👩‍🦰', callback_data='woman1.1')]])





target = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Поддержание', callback_data='maintenance1'),
                                                InlineKeyboardButton(text='Похудение', callback_data='weight_loss1')],
                                                [InlineKeyboardButton(text='Набор', callback_data='kit1')]])

target1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Поддержание', callback_data='maintenance1.1'),
                                                InlineKeyboardButton(text='Похудение', callback_data='weight_loss1.1')],
                                                [InlineKeyboardButton(text='Набор', callback_data='kit1.1')]])

target2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Поддержание', callback_data='maintenance2'),
                                                InlineKeyboardButton(text='Похудение', callback_data='weight_loss2')],
                                                [InlineKeyboardButton(text='Набор', callback_data='kit2')]])

target2girl = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Поддержание', callback_data='maintenance2.1'),
                                                InlineKeyboardButton(text='Похудение', callback_data='weight_loss2.1')],
                                                [InlineKeyboardButton(text='Набор', callback_data='kit2.1')]])




# Набор

experience = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three')]])

experience1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One1'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree1')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three1')]])

# похудение

experience2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One2'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree2')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three2')]])

experience21 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One21'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree21')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three21')]])


# поддержание 
experience3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One3'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree3')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three3')]])

experience31 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='< 1 года', callback_data='One31'),
                                                    InlineKeyboardButton(text='1-3 года', callback_data='OneThree31')],
                                                    [InlineKeyboardButton(text='> 3 лет', callback_data='Three31')]])