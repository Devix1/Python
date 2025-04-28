from email import message
import types
from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb


router = Router()




@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('🌟 Добро пожаловать в Training Plan 🌟 \n\nТы готов изменить свою жизнь и достичь своих фитнес-целей? 💪🥗\n\nНаш бот — твой личный тренер и диетолог, доступный 24/7! \n\n🔹 Что мы предлагаем?\n- Персонализированные планы тренировок для любого уровня подготовки: от новичка до профи!\n- Индивидуальные планы питания, которые помогут тебе достичь желаемых результатов: набор массы, похудение или поддержание веса.\n- Удобный и простой интерфейс: всего несколько кликов — и твой план готов!\n\n🔹 Как это работает?\n1. Напиши команду /start, чтобы начать.\n2. Выбери, что тебя интересует: план тренировок или план питания.\n3. Ответь на несколько простых вопросов о своем поле, цели и стаже тренировок.\n4. Получи свой персонализированный план и начни двигаться к своей цели!\n\n🎯 Не упусти шанс стать лучше!\nПрисоединяйся к нам и начни свой путь к идеальному телу уже сегодня!\n\n👉 Training Plan — твой надежный помощник в мире фитнеса! \n\n💬 Напиши нам и начни свой путь к успеху!' , reply_markup=kb.main)

@router.message(Command('tgk'))
async def cmd_tgk(message: Message):
    await message.answer('Не забудь подписаться \n https://t.me/freekazuketr')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('По всем вопросам вы можете обраться к @Freekazuke ')


@router.message(F.text == 'Получить планы 🗒️')
async def plans(message: Message):
    await message.answer('Выбирите план, который хотите получить:', reply_markup=kb.plans)

@router.message(F.text == 'Наш телеграмм канал ✉️')
async def Tgk(message: Message):
    await message.answer('Не забудь подписаться! \n https://t.me/freekazuketr')






@router.callback_query(F.data == 'trainingPlan')
async def trainingPlan(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Ваш пол?', reply_markup=kb.floor1)

@router.callback_query(F.data == 'foodPlan')
async def foodPlan(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Ваш пол?', reply_markup=kb.floor)




@router.callback_query(F.data == 'men1')
async def men1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Мужской \n Ваша цель? ', reply_markup=kb.target2)

@router.callback_query(F.data == 'woman1')
async def men1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Женский \n Ваша цель? ', reply_markup=kb.target2girl)

@router.callback_query(F.data == 'men1.1')
async def men1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель? ', reply_markup=kb.target1)

@router.callback_query(F.data == 'woman1.1')
async def men1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель? ', reply_markup=kb.target)













@router.callback_query(F.data == 'maintenance2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Мужской \n Ваша цель: Поддержание \n Введите свой нынешний вес:')

@router.callback_query(F.data == 'weight_loss2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Мужской \n Ваша цель: Похудение \n Введите свой нынешний вес: ' )

@router.callback_query(F.data == 'kit2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания\n Пол: Мужской \n Ваша цель: Набор \n Введите свой нынешний вес:' )


@router.callback_query(F.data == 'maintenance2.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Женский \n Ваша цель: Поддержание \n Введите свой нынешний вес: ' )

@router.callback_query(F.data == 'weight_loss2.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Женский \n Ваша цель: Похудение \n Введите свой нынешний вес:' )

@router.callback_query(F.data == 'kit2.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: План питания \n Пол: Женский \n Ваша цель: Набор \n Введите свой нынешний вес:  ')















@router.callback_query(F.data == 'maintenance1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Поддержание \n Ваш стаж? '
                                  , reply_markup=kb.experience3)

@router.callback_query(F.data == 'weight_loss1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Похудение \n Ваш стаж? '
                                  , reply_markup=kb.experience2)

@router.callback_query(F.data == 'kit1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Набор \n Ваш стаж? '
                                  , reply_markup=kb.experience)


@router.callback_query(F.data == 'maintenance1.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Поддержание \n Ваш стаж? '
                                  , reply_markup=kb.experience31)

@router.callback_query(F.data == 'weight_loss1.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Похудение \n Ваш стаж? '
                                  , reply_markup=kb.experience21)

@router.callback_query(F.data == 'kit1.1')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Набор \n Ваш стаж? '
                                  , reply_markup=kb.experience1)







@router.callback_query(F.data == 'One')
async def one(callback: CallbackQuery):
    file_patch = 'W:\Code\Работы\TG\TGBotPython'
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Набор \n Ваш стаж: < 1 года\n Вот ваш план тренировки: ' )
@router.callback_query(F.data == 'OneThree')
async def one(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Набор \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three')
async def one(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Набор \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:')

@router.callback_query(F.data == 'One1')
async def one(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Набор \n Ваш стаж: < 1 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'OneThree1')
async def one(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской  \n Ваша цель: Набор \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three1')
async def one(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Набор \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:')







@router.callback_query(F.data == 'One2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Похудение \n Ваш стаж: > 1 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'OneThree2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Похудение \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three2')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Похудение \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:')

@router.callback_query(F.data == 'One21')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Похудение \n Ваш стаж: > 1 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'OneThree21')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Похудение \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three21')
async def maintenance1(callback: CallbackQuery): 
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Похудение \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:')
    

@router.callback_query(F.data == 'One3')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Поддержание \n Ваш стаж: < 1 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'OneThree3')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Поддержание \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three3')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Женский \n Ваша цель: Поддержание \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:')

@router.callback_query(F.data == 'One31')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Поддержание \n Ваш стаж: < 1 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'OneThree31')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Поддержание \n Ваш стаж: 1-3 года\n Вот ваш план тренировки:')
@router.callback_query(F.data == 'Three31')
async def maintenance1(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию!')
    await callback.message.answer('Категория: Тренировочный план \n Пол: Мужской \n Ваша цель: Поддержание \n Ваш стаж: > 3 лет\n Вот ваш план тренировки:' )
