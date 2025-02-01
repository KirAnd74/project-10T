
from aiogram import Router, F

from aiogram.filters import CommandStart, Command, or_f

from aiogram.types import Message

from aiogram.fsm.context import FSMContext


from kbds import reply

from kbds.generators import generate

from kbds.state import Work


user_private_router = Router()


# Define URLs for OGE and EGE tasks

oge_urls = {

    "🖊️1": "https://telegra.ph/Zadanie-1-Kolichestvennye-parametry-informacionnyh-obektov-11-04",

    "🖊️2": "https://telegra.ph/Zadanie-2-Kodirovanie-i-dekodirovanie-informacii-11-04",

    "🖊️3": "https://telegra.ph/Zadanie-3-Znachenie-logicheskogo-vyrazheniya-11-04",

    "🖊️4": "https://telegra.ph/Zadanie-4Formalnye-opisaniya-realnyh-obektov-i-processov-11-04",

    "🖊️5": "https://telegra.ph/Zadanie-5-Prostoj-linejnyj-algoritm-dlya-formalnogo-11-04",

    "🖊️6": "https://telegra.ph/Zadanie-6-Programma-s-uslovnym-operatorom-11-13",

    "🖊️7": "https://telegra.ph/Zadanie-7-Informacionno-kommunikacionnye-tehnologii-11-13",

    "🖊️8": "https://telegra.ph/Zadanie-8-Zaprosy-dlya-poiskovyh-sistem-s-ispolzovaniem-logicheskih-vyrazhenij-11-13",

    "🖊️9": "https://telegra.ph/Zadanie-5-Analizirovanie-informacii-predstavlennoj-v-vide-shem-11-13",

    "🖊️10": "https://telegra.ph/Zadanie-10-Sravnenie-chisel-v-razlichnyh-sistemah-schisleniya-11-13",

    "🖊️11": "https://telegra.ph/Zadanie-11-Ispolzovanie-poiska-operacionnoj-sistemy-i-tekstovogo-redaktora-11-13",

    "🖊️12": "https://telegra.ph/Zadanie-12-Ispolzovanie-poiskovyh-sredstv-operacionnoj-sistemy-11-13",

    "🖊️13": "13.1: \n https://telegra.ph/Zadanie-131-Sozdanie-prezentacii-11-18 \n 13.2: \n https://telegra.ph/Zadanie-132-Formatirovanie-teksta-11-18",

    "🖊️14": "https://telegra.ph/Zadanie-14-Obrabotka-bolshogo-massiva-dannyh-11-18",

    "🖊️15": "15.1: \n https://telegra.ph/Zadanie-151-Korotkij-algoritm-v-razlichnyh-sredah-ispolneniya-11-18 \n 15.2:\n https://telegra.ph/Zadanie-152-Programmirovanie-11-18",

}
oge_urls2 = {
    "📔1":"Вариант 1: https://telegra.ph/Variant-1-01-19-2",
    "📔2":"Вариант 2: https://telegra.ph/Variant-2-01-19",
    "📔3":"Вариант 3:https://telegra.ph/Variant-3-01-19-2",
    "📔4":"Вариант 4:https://telegra.ph/Variant-4-01-19",
}


ege_urls = {

    "✏️1": "https://telegra.ph/Zadanie-1-Analiz-informacionnyh-modelej-11-18",

    "✏️2": "https://telegra.ph/Zadanie-2Postroenie-tablic-istinnosti-logicheskih-vyrazhenij-11-19",

    "✏️3": "https://telegra.ph/Zadanie-3-11-19",

    "✏️4": "https://telegra.ph/Zadanie-4-Kodirovanie-i-dekodirovanie-informacii-11-19",

    "✏️5": "https://telegra.ph/Zadanie-5-Analiz-i-postroenie-algoritmov-dlya-ispolnitelej-11-19",

    "✏️6": "https://telegra.ph/Zadanie-6-Opredelenie-rezultatov-raboty-prostejshih-algoritmov-11-19",

    "✏️7": "https://telegra.ph/Zadanie-7-Kodirovanie-i-dekodirovanie-informacii-Peredacha-informacii-11-19",

    "✏️8": "https://telegra.ph/Zadanie-8Perebor-slov-i-sistemy-schisleniya-11-19",

    "✏️9": "https://telegra.ph/Zadanie-9-Rabota-s-tablicami-11-19",

    "✏️10": "https://telegra.ph/Zadanie-10-Poisk-simvolov-v-tekstovom-redaktore-11-19",

    "✏️11": "https://telegra.ph/Zadanie-11-Vychislenie-kolichestva-informacii-11-19",

    "✏️12": "https://telegra.ph/Zadanie-12Vypolnenie-algoritmov-dlya-ispolnitelej-11-19",

    "✏️13": "https://telegra.ph/Zadanie-13Organizaciya-kompyuternyh-setej-Adresaciya-11-20",

    "✏️14": "https://telegra.ph/Zadanie-14Kodirovanie-chisel-Sistemy-schisleniya-11-20",

    "✏️15": "https://telegra.ph/Zadanie-15Preobrazovanie-logicheskih-vyrazhenij-11-20",

    "✏️16": "https://telegra.ph/Zadanie-16Rekursivnye-algoritmy-11-20",

    "✏️17": "https://telegra.ph/Zadanie-17Obrabotki-chislovoj-posledovatelnosti-11-20",

    "✏️18": "https://telegra.ph/Zadanie-18Robot-sborshchik-monet-11-20",

    "✏️19": "https://telegra.ph/Zadanie-19Vyigryshnaya-strategiya-Zadanie-1-11-20",

    "✏️20": "https://telegra.ph/Zadanie-20Vyigryshnaya-strategiya-Zadanie-2-11-20",

    "✏️21": "https://telegra.ph/Zadanie-21Vyigryshnaya-strategiya-Zadanie-3-11-20",

    "✏️22": "https://telegra.ph/Zadanie-22Mnogoprocessornye-sistemy-02-01",

    "✏️23": "https://telegra.ph/Zadanie-23Operator-prisvaivaniya-i-vetvleniya-Perebor-variantov-postroenie-dereva-11-20",

    "✏️24": "https://telegra.ph/Zadanie-24Obrabotka-simvolnyh-strok-11-20",

    "✏️25": "https://telegra.ph/Zadanie-25Obrabotka-celochislennoj-informacii-02-01",

    "✏️26": "https://telegra.ph/Zadanie-12Vypolnenie-algoritmov-dlya-ispolnitelej-11-20",

    "✏️27": "https://telegra.ph/Zadanie-27Programmirovanie-11-20",

}
ege_urls2 = {
    "📓1":"Вариант 1: https://telegra.ph/Variant-1-01-25",
    "📓2":"Вариант 2: https://telegra.ph/Variant-1-01-25-2",
    "📓3":"Вариант 3: https://telegra.ph/Variant-3-01-25",
    "📓4":"Вариант 4: https://telegra.ph/Variant-4-01-25 \n Продолжение: https://telegra.ph/Variant-42-01-25",
}

@user_private_router.message(CommandStart())

async def start_cmd(message: Message):

    await message.answer("Привет я бот для подготовки к экзаменам по информатике", reply_markup=reply.start_kb)


@user_private_router.message(F.text == "Назад")

async def menu(message: Message):

    await start_cmd(message)


@user_private_router.message(or_f(Command("oge"), (F.text == "ОГЭ")))  # OGE

async def menu(message: Message):

    await message.answer(

        "Хорошо!\nТеперь я расскажу как устроен бот, если нажать Разбор заданий, ты увидишь разбор всех заданий.\nЕсли нажать на Практика, то сможешь решать примеры заданий",

        reply_markup=reply.oge_kb,

    )

@user_private_router.message(or_f(Command("help"), (F.text == "Помощь")))

async def menu(message: Message):
    await message.answer("Если возникли вопросы или предложения по улучшению, можете написать мне: \n @kirand21a  ", reply_markup=reply.help_kb)


@user_private_router.message(F.text == "Разбор заданий")

async def menu(message: Message):

    await message.answer("Выбери номер задания", reply_markup=reply.oge_razbor_kb)


@user_private_router.message(F.text == "Практика")

async def menu(message: Message):

    await message.answer(

        "Готов по практиковаться?\nВ этом блоке будут и простые и сложные задачи.",

        reply_markup=reply.oge_practika_kb,

    )


# Handler for OGE task URLs

@user_private_router.message(F.text.lower().in_(oge_urls.keys()))

async def handle_oge_tasks(message: Message):

    url = oge_urls[message.text.lower()]

    await message.answer(url, reply_markup=reply.oge_razbor_kb)
@user_private_router.message(F.text.lower().in_(oge_urls2.keys()))

async def handle_oge_tasks(message: Message):

    url = oge_urls2[message.text.lower()]

    await message.answer(url, reply_markup=reply.oge_practika_kb)


# Handler for EGE commands

@user_private_router.message(or_f(Command("ege"), (F.text == "ЕГЭ")))  # EGE

async def menu(message: Message):

    await message.answer(

        "Хорошо!\nТеперь я расскажу как устроен бот, если нажать Разбор заданий, ты увидишь разбор всех заданий.\nЕсли нажать на Практика, то сможешь решать примеры заданий",

        reply_markup=reply.ege_kb,

    )


@user_private_router.message(F.text == "✏️Разбор заданий")

async def menu(message: Message):

    await message.answer("Выбери номер задания:\nстраница №1", reply_markup=reply.ege_razbor_str1_kb)

@user_private_router.message(F.text == "✏️Практика")
async def menu(message: Message):
    await message.answer(
        f"Готов по практиковаться?\n В этом блоке будут и просты и сложные задачи. ",
        reply_markup=reply.ege_practika_kb,)


# Handler for EGE task URLs

@user_private_router.message(F.text.lower().in_(ege_urls.keys()))

async def handle_ege_tasks(message: Message):

    url = ege_urls[message.text.lower()]

    await message.answer(url, reply_markup=reply.ege_razbor_str1_kb)
@user_private_router.message(F.text.lower().in_(ege_urls2.keys()))

async def handle_ege_tasks(message: Message):

    url = ege_urls2[message.text.lower()]

    await message.answer(url, reply_markup=reply.ege_practika_kb)
    
@user_private_router.message(F.text == "🔙Назад")
async def menu(message: Message):
    await message.answer(
        "Хорошо!\nТеперь я расскажу как устроен бот , если нажать  Разбор заданий , ты увидишь  разбор всех заданий.\nЕсли нажать на Практика , то сможешь решать  примеры заданий",
        reply_markup=reply.oge_kb,
    )
@user_private_router.message(F.text == "◀️Назад")
async def menu(message: Message):
    await message.answer(
        "Хорошо!\nТеперь я расскажу как устроен бот , если нажать  Разбор заданий , ты увидишь  разбор всех заданий.\nЕсли нажать на Практика , то сможешь решать  примеры заданий",
        reply_markup=reply.ege_kb,
    )


@user_private_router.message(F.text == "➡️Далее")
async def menu(message: Message):
    await message.answer(
        "страница №2",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text == "⬅️Назад")
async def menu(message: Message):
    await message.answer(
        "Выбери номер задания:\nстраница №1",
        reply_markup=reply.ege_razbor_str1_kb,
    )


# AI bot command handling

@user_private_router.message()

async def ai(message: Message, state: FSMContext):

    res = await generate(message.text)

    await message.answer(res.choices[0].message.content, reply_markup=reply.ai_kb)

    await state.clear()


@user_private_router.message(Work.process)

async def stop(message: Message):

    await message.answer("Подождите, идет обработка задания")