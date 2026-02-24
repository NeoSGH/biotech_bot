from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

last_bot_message = {}

# --- Клавиатуры ---

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📹 Видео-уроки"),
    KeyboardButton("📝 Тесты к урокам")
)
main_menu.add(
    KeyboardButton("ℹ️ О проекте"),
    KeyboardButton("✉️ Обратная связь")
)

back_menu = ReplyKeyboardMarkup(resize_keyboard=True)
back_menu.add(KeyboardButton("🔙 Вернуться в начало"))

# --- Видео-уроки ---

video_menu = ReplyKeyboardMarkup(resize_keyboard=True)
video_menu.add(
    KeyboardButton("1️⃣ Генетика. Законы Грегора Менделя."),
    KeyboardButton("2️⃣ Клеточный цикл. Митоз и мейоз.")
)
video_menu.add(
    KeyboardButton("3️⃣ Эволюция. Дарвин и другие."),
    KeyboardButton("4️⃣ Наследственные болезни человека: классификация и методы лечения.")
)
video_menu.add(
    KeyboardButton("5️⃣ Микробиология: ДНК, РНК и синтез белка."),
    KeyboardButton("6️⃣ Урок 6 (в разработке)")
)
video_menu.add(
    KeyboardButton("7️⃣ Урок 7 (в разработке)"),
    KeyboardButton("8️⃣ Урок 8 (в разработке)")
)
video_menu.add(KeyboardButton("🔙 Вернуться в начало"))

# --- Тесты ---

test_menu = ReplyKeyboardMarkup(resize_keyboard=True)
test_menu.add(
    KeyboardButton("🧬 Тест 1: Законы Грегора Менделя"),
    KeyboardButton("🧪 Тест 2 (в разработке)")
)
test_menu.add(
    KeyboardButton("🧪 Тест 3 (в разработке)"),
    KeyboardButton("🧪 Тест 4 (в разработке)")
)
test_menu.add(
    KeyboardButton("🧪 Тест 5 (в разработке)"),
    KeyboardButton("🧪 Тест 6 (в разработке)")
)
test_menu.add(
    KeyboardButton("🧪 Тест 7 (в разработке)"),
    KeyboardButton("🧪 Тест 8 (в разработке)")
)
test_menu.add(KeyboardButton("🔙 Вернуться в начало"))

# --- Вспомогательная функция ---

async def send_clean_message(message: types.Message, text: str, keyboard):
    user_id = message.from_user.id

    if user_id in last_bot_message:
        try:
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=last_bot_message[user_id]
            )
        except:
            pass

    if message.text != "/start":
        try:
            await message.delete()
        except:
            pass

    sent = await message.answer(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
    last_bot_message[user_id] = sent.message_id

# --- Хэндлеры ---

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await send_clean_message(
        message,
        "Добро пожаловать!\nВыберите нужную функцию по кнопкам ниже 👇",
        main_menu
    )

# --- Видео ---

@dp.message_handler(lambda message: message.text == "📹 Видео-уроки")
async def video_lessons(message: types.Message):
    await send_clean_message(
        message,
        "Выберите видео-урок 📚",
        video_menu
    )

@dp.message_handler(lambda message: message.text == "1️⃣ Генетика. Законы Грегора Менделя.")
async def lesson_mendel(message: types.Message):
    await send_clean_message(
        message,
        "🌿 Урок 1:\n"
        "Генетика. Законы Грегора Менделя\n\n"
        "https://youtu.be/I9KD2YcJxaU?si=Le2pz90J4dNxbzJa",
        back_menu
    )

@dp.message_handler(lambda message: message.text == "2️⃣ Клеточный цикл. Митоз и мейоз.")
async def lesson_cell_cycle(message: types.Message):
    await send_clean_message(
        message,
        "🌱 Урок 2:\n"
        "Клеточный цикл. Митоз и мейоз\n\n"
        "https://youtu.be/kcc0-FpuiTw?si=p5V9nZhZyiTE1ZNT",
        back_menu
    )

@dp.message_handler(lambda message: message.text == "3️⃣ Эволюция. Дарвин и другие.")
async def lesson_cell_cycle(message: types.Message):
    await send_clean_message(
        message,
        "🌱 Урок 3:\n"
        "Эволюция: теории и учения.\n\n"
        "https://youtu.be/FJgCAQy3ttE",
        back_menu
    )

@dp.message_handler(lambda message: message.text == "4️⃣ Наследственные болезни человека: классификация и методы лечения.")
async def lesson_cell_cycle(message: types.Message):
    await send_clean_message(
        message,
        "🌱 Урок 4:\n"
        "Наследственные болезни человека: классификация и методы лечения.\n\n"
        "https://youtu.be/gDDN6pF1Oew",
        back_menu
    )

@dp.message_handler(lambda message: message.text == "5️⃣ Микробиология: ДНК, РНК и синтез белка.")
async def lesson_cell_cycle(message: types.Message):
    await send_clean_message(
        message,
        "🌱 Урок 5:\n"
        "Микробиология: ДНК, РНК и синтез белка.\n\n"
        "https://youtu.be/jAJYekle3MY",
        back_menu
    )

# Пустышки уроков
@dp.message_handler(lambda message: "Урок" in message.text and "разработке" in message.text)
async def empty_lessons(message: types.Message):
    await send_clean_message(
        message,
        "Этот урок скоро появится 🌿\nСледите за обновлениями.",
        back_menu
    )

# --- Тесты ---

@dp.message_handler(lambda message: message.text == "📝 Тесты к урокам")
async def tests_menu(message: types.Message):
    await send_clean_message(
        message,
        "Выберите тест для проверки знаний 🧠",
        test_menu
    )

@dp.message_handler(lambda message: message.text == "🧬 Тест 1: Законы Грегора Менделя")
async def test_mendel(message: types.Message):
    await send_clean_message(
        message,
        "🧪 Тест по теме «Законы Грегора Менделя»:\n\n"
        "https://forms.gle/SKaReKaXnxSkPGDC7",
        back_menu
    )

# Пустышки тестов
@dp.message_handler(lambda message: "Тест" in message.text and "разработке" in message.text)
async def empty_tests(message: types.Message):
    await send_clean_message(
        message,
        "Этот тест пока в разработке 🧠\nОн скоро появится.",
        back_menu
    )

# --- Инфо и обратная связь ---

@dp.message_handler(lambda message: message.text in [
    "ℹ️ О проекте",
    "✉️ Обратная связь"
])
async def info_and_feedback(message: types.Message):
    if message.text == "✉️ Обратная связь":
        await send_clean_message(
            message,
            "Если вы нашли ошибку или у вас есть предложение,\n"
            "напишите нам на почту:\n"
            "krivonos.artyom.a@gmail.com",
            back_menu
        )
    else:
        await send_clean_message(
            message,
            "Этот проект — бот-репетитор по биологии 🌱\n"
            "Видео, объяснения и тесты для закрепления знаний.\n"
            "    \n"
            "Авторы данного проекта: ученики 10В класса КГУ Гимназии №34, Кривонос Артём и Сарсенказы Алибек.\n"
            "Научныый руководитель проекта: Алыбаева Лилиана Яковлевна.",
            back_menu
        )

@dp.message_handler(lambda message: message.text == "🔙 Вернуться в начало")
async def back_to_start(message: types.Message):
    await send_clean_message(
        message,
        "Добро пожаловать!\nВыберите нужную функцию по кнопкам ниже 👇",
        main_menu
    )


# --- Запуск ---

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
