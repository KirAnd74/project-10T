from aiogram import Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from aiogram.fsm.storage.memory import SimpleEventIsolation

from kbds import reply, inline
from kbds.generators import generate
from kbds.state import Work


 #class Practika_Oge(Scene , state = 'menu'):


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Привет я бот для подготовки к экзаменам по информатике", reply_markup=reply.start_kb)


@user_private_router.message((F.text == "Назад"))
async def menu(message: Message):
    await message.answer("Привет я бот для подготовки к экзаменам по информатике", reply_markup=reply.start_kb)


# aibot"start"
@user_private_router.message((F.text == "аи"))
async def ai(message: Message, state: FSMContext):
    res = await generate(message.text)
    await message.answer(res.choices[0].message.content, reply_markup=reply.ai_kb)
    await state.clear()


@user_private_router.message(Work.process)
async def stop(message: Message):
    await message.answer("Подождите, идет обработка задания")


# aibot"end"


@user_private_router.message(or_f(Command("oge"), (F.text == "ОГЭ")))  # OGE
async def menu(message: Message):
    await message.answer(
        "Хорошо!\nТеперь я расскажу как устроен бот , если нажать  Разбор заданий , ты увидишь  разбор всех заданий.\nЕсли нажать на Практика , то сможешь решать  примеры заданий",
        reply_markup=reply.oge_kb,
    )


@user_private_router.message(F.text == "Разбор заданий")
async def menu(message: Message):
    await message.answer("Выбери номер задания", reply_markup=reply.oge_razbor_kb)


@user_private_router.message(F.text == "🔙Назад")
async def menu(message: Message):
    await message.answer(
        "Хорошо!\nТеперь я расскажу как устроен бот , если нажать  Разбор заданий , ты увидишь  разбор всех заданий.\nЕсли нажать на Практика , то сможешь решать  примеры заданий",
        reply_markup=reply.oge_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️1")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-1-Kolichestvennye-parametry-informacionnyh-obektov-11-04",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️2")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-2-Kodirovanie-i-dekodirovanie-informacii-11-04", reply_markup=reply.oge_razbor_kb
    )


@user_private_router.message(F.text.lower() == "🖊️3")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-3-Znachenie-logicheskogo-vyrazheniya-11-04", reply_markup=reply.oge_razbor_kb
    )


@user_private_router.message(F.text.lower() == "🖊️4")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-4Formalnye-opisaniya-realnyh-obektov-i-processov-11-04",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️5")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-5-Prostoj-linejnyj-algoritm-dlya-formalnogo-11-04",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️6")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-6-Programma-s-uslovnym-operatorom-11-13", reply_markup=reply.oge_razbor_kb
    )


@user_private_router.message(F.text.lower() == "🖊️7")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-7-Informacionno-kommunikacionnye-tehnologii-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️8")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-8-Zaprosy-dlya-poiskovyh-sistem-s-ispolzovaniem-logicheskih-vyrazhenij-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️9")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-5-Analizirovanie-informacii-predstavlennoj-v-vide-shem-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️10")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-10-Sravnenie-chisel-v-razlichnyh-sistemah-schisleniya-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️11")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-11-Ispolzovanie-poiska-operacionnoj-sistemy-i-tekstovogo-redaktora-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️12")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-12-Ispolzovanie-poiskovyh-sredstv-operacionnoj-sistemy-11-13",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️13")
async def menu(message: Message):
    await message.answer(
        f"13.1: \n https://telegra.ph/Zadanie-131-Sozdanie-prezentacii-11-18 \n 13.2: \n https://telegra.ph/Zadanie-132-Formatirovanie-teksta-11-18",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text.lower() == "🖊️14")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-14-Obrabotka-bolshogo-massiva-dannyh-11-18", reply_markup=reply.oge_razbor_kb
    )


@user_private_router.message(F.text.lower() == "🖊️15")
async def menu(message: Message):
    await message.answer(
        f"15.1: \n https://telegra.ph/Zadanie-151-Korotkij-algoritm-v-razlichnyh-sredah-ispolneniya-11-18 \n 15.2:\n https://telegra.ph/Zadanie-152-Programmirovanie-11-18",
        reply_markup=reply.oge_razbor_kb,
    )


@user_private_router.message(F.text == "Практика")
async def menu(message: Message):
    await message.answer(
        f"Готов по практиковаться?\n В этом блоке будут и просты и сложные задачи. ",
        reply_markup=reply.oge_practika_kb,
    )


@user_private_router.message(F.text == "📔1")
async def menu(message: Message):
    await message.answer(
        f"Выберете номер задания:",
        reply_markup=inline.og_pr1_kb,
    )


@user_private_router.callback_query(F.data == "1")
async def menu(callback: CallbackQuery):
    await callback.message.answer(
        f"Задача №1\nВ кодировке КОИ-8 каждый символ кодируется 8 битами.\n Аня написала текст (в нем нет лишних пробелов)\n:«ерш, Щука, Бычок, Карась, Гимнура, Долгопер  — рыбы».\nУченик вычеркнул из списка название одной из рыб. Заодно он вычеркнул ставшие лишними запятые и пробелы  — два пробела не должны идти подряд.При этом размер нового предложения в данной кодировке оказался на 10 байтов меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название рыбы.Введите ответ:",
        reply_markup=reply.og_pr1_kb,
    )


@user_private_router.message(or_f(Command("ege"), (F.text == "ЕГЭ")))  # ЕGE
async def menu(message: Message):
    await message.answer(
        "Хорошо!\nТеперь я расскажу как устроен бот , если нажать  Разбор заданий , ты увидишь  разбор всех заданий.\nЕсли нажать на Практика , то сможешь решать  примеры заданий",
        reply_markup=reply.ege_kb,
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


@user_private_router.message(F.text == "✏️Разбор заданий")
async def menu(message: Message):
    await message.answer(f"Выбери номер задания:\nстраница №1", reply_markup=reply.ege_razbor_str1_kb)


@user_private_router.message(F.text.lower() == "✏️1")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-1-Analiz-informacionnyh-modelej-11-18",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️2")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-2Postroenie-tablic-istinnosti-logicheskih-vyrazhenij-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️3")
async def menu(message: Message):
    await message.answer("https://telegra.ph/Zadanie-3-11-19", reply_markup=reply.ege_razbor_str1_kb)


@user_private_router.message(F.text.lower() == "✏️4")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-4-Kodirovanie-i-dekodirovanie-informacii-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️5")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-5-Analiz-i-postroenie-algoritmov-dlya-ispolnitelej-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️6")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-6-Opredelenie-rezultatov-raboty-prostejshih-algoritmov-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️7")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-7-Kodirovanie-i-dekodirovanie-informacii-Peredacha-informacii-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️8")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-8Perebor-slov-i-sistemy-schisleniya-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️9")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-9-Rabota-s-tablicami-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️10")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-10-Poisk-simvolov-v-tekstovom-redaktore-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️11")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-11-Vychislenie-kolichestva-informacii-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️12")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-12Vypolnenie-algoritmov-dlya-ispolnitelej-11-19",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️13")
async def menu(message: Message):
    await message.answer(
        f"https://telegra.ph/Zadanie-13Organizaciya-kompyuternyh-setej-Adresaciya-11-20",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️14")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-14Kodirovanie-chisel-Sistemy-schisleniya-11-20",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️15")
async def menu(message: Message):
    await message.answer(
        f"https://telegra.ph/Zadanie-15Preobrazovanie-logicheskih-vyrazhenij-11-20",
        reply_markup=reply.ege_razbor_str1_kb,
    )


@user_private_router.message(F.text.lower() == "✏️16")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-16Rekursivnye-algoritmy-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️17")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-17Obrabotki-chislovoj-posledovatelnosti-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️18")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-18Robot-sborshchik-monet-11-20", reply_markup=reply.ege_razbor_str2_kb
    )


@user_private_router.message(F.text.lower() == "✏️19")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-19Vyigryshnaya-strategiya-Zadanie-1-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️20")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-20Vyigryshnaya-strategiya-Zadanie-2-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️21")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-21Vyigryshnaya-strategiya-Zadanie-3-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️22")
async def menu(message: Message):
    await message.answer(
        "",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️23")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-23Operator-prisvaivaniya-i-vetvleniya-Perebor-variantov-postroenie-dereva-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️24")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-24Obrabotka-simvolnyh-strok-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️25")
async def menu(message: Message):
    await message.answer(
        "",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️26")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-12Vypolnenie-algoritmov-dlya-ispolnitelej-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )


@user_private_router.message(F.text.lower() == "✏️27")
async def menu(message: Message):
    await message.answer(
        "https://telegra.ph/Zadanie-27Programmirovanie-11-20",
        reply_markup=reply.ege_razbor_str2_kb,
    )
