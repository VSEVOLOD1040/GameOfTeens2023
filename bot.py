import telebot
import config

bot = telebot.TeleBot(config.token)
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def keyboard_start():
    markup = ReplyKeyboardMarkup()
    itembtn1 = KeyboardButton('ПОЧАТИ 🚩')

    markup.add(itembtn1)
    return markup

def keyboard_gotostart():
    markup = ReplyKeyboardMarkup()
    itembtn1 = KeyboardButton('НА ПОЧАТОК 🏡')

    markup.add(itembtn1)
    return markup


def first():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton('Підібрати тариф 💵', callback_data="tarifound")
    itembtn5 = InlineKeyboardButton('Перейти від іншого оператора зі збереженням номера🔃', url="https://mnp.lifecell.ua/uk/?_ga=2.264227532.1504623844.1686927457-1729857917.1686927457")


    markup.add(itembtn4)
    markup.row(itembtn5)
    return markup

def tarifor():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Телефону 📱", callback_data="phone")
    i5 = InlineKeyboardButton('Іншого пристрою 💻', callback_data="other")


    markup.add(i4, i5)

    return markup

def family():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Так ✅", callback_data="yes")
    i5 = InlineKeyboardButton('Ні ❌', callback_data="no")


    markup.add(i4, i5)

    return markup

def nf():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton("Сигналізація 🚓", url=config.signalisation)
    itembtn5 = InlineKeyboardButton('Смарт годинник ⌚', url=config.watch)
    itembtn6 = InlineKeyboardButton("Планшет 💻", url=config.tablet)
    itembtn7 = InlineKeyboardButton("Роутер 🌐", url=config.router)

    markup.row(itembtn4, itembtn5)
    markup.row(itembtn6, itembtn7)
    return markup

def family2():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton('500хв, 20гб, 500смс - 375грн', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/")
    itembtn5 = InlineKeyboardButton('750хв, 30гб, 1000смс - 425грн', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/")
    itembtn6 = InlineKeyboardButton('1500хв, 50гб, 1500смс - 500грн', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/")

    markup.add(itembtn4)
    markup.row(itembtn5)
    markup.row(itembtn6)
    return markup

def ss():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton('Студента 👨‍🎓', callback_data="student")
    itembtn5 = InlineKeyboardButton('Школяра 🏢', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/")
    itembtn6 = InlineKeyboardButton('Інше', callback_data="other/2")

    markup.row(itembtn4, itembtn5)

    markup.add(itembtn6)
    return markup

def student():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton('1600хв, Безлімітний інтернет, 180грн', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/")
    itembtn5 = InlineKeyboardButton('800хв, 25гб, 120грн', url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/")
    itembtn6 = InlineKeyboardButton("300хв, 8гб, 90грн", url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/")

    markup.add(itembtn4)
    markup.row(itembtn5)
    markup.row(itembtn6)
    return markup

def ft():
    markup = InlineKeyboardMarkup()
    itembtn4 = InlineKeyboardButton("1600хв, Безлімітний інтернет, 180грн", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/')
    itembtn5 = InlineKeyboardButton('800хв, 25гб - 120грн', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/')
    itembtn6 = InlineKeyboardButton("300хв, 8гб - 90грн", url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/")
    itembtn7 = InlineKeyboardButton("3000хв, Безлімітний інтернет, 50смс - 250грн", url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/")

    markup.row(itembtn4)
    markup.row(itembtn5)
    markup.row(itembtn6)
    markup.row(itembtn7)
    return markup


def create():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Створити свій тариф 🛠", url="https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/")
    i5 = InlineKeyboardButton('Обрати готовий тариф 🏪', callback_data="skip")


    markup.add(i4, i5)

    return markup

def friends():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Так ✅", callback_data="yes/f")
    i5 = InlineKeyboardButton('Ні ❌', callback_data="no/f")


    markup.add(i4, i5)

    return markup

def friends3():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Безлімітний інтернет 😎", callback_data="ui")
    i5 = InlineKeyboardButton('8 - 25гб інтернету 🙂', callback_data="825")


    markup.row(i4)
    markup.row(i5)

    return markup


def friends825():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Смарт Лайф", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/')
    i5 = InlineKeyboardButton('Просто Лайф', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/')


    markup.add(i4, i5)

    return markup

def friendsui():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("Вільний Лайф", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/')
    i5 = InlineKeyboardButton('Platinum Лайф', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/')


    markup.add(i4, i5)

    return markup

def best():
    markup = InlineKeyboardMarkup()
    i4 = InlineKeyboardButton("ТАК 😎", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/')
    i5 = InlineKeyboardButton('Дайте більше пропозицій ☝', callback_data="no/b")


    markup.add(i4, i5)

    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text:
        print(message.from_user.last_name, message.from_user.first_name, ": IS STARTING, userID:", message.from_user)
        bot.send_message(message.chat.id,
                         f"Добрий день {message.from_user.first_name}, цей бот допоможе вам зорієнтуватись у пропозиціях Lifecell 🐝",
                         reply_markup=keyboard_start())


@bot.message_handler(commands=['test'])
def test(message):
    if message.text:
        a = message.text
        print(a)


@bot.message_handler(content_types=['text'])
def conversation(message):
    if message.text == "ПОЧАТИ 🚩":
        print(message.from_user.last_name, message.from_user.first_name, ":", message.text)
        bot.send_message(message.chat.id, "Ми раді, що ви обрали Lifecell 🤗", reply_markup=keyboard_gotostart())
        bot.send_message(message.chat.id, "Ви бажаєте:", reply_markup=first())
    if message.text == "НА ПОЧАТОК 🏡":
        print(message.from_user.last_name, message.from_user.first_name, ":", message.text)
        bot.send_message(message.chat.id, "Ви бажаєте:", reply_markup=first())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "othernum":
        bot.send_message(call.from_user.id, "Перейдіть за посиланням, щоб це зробити ↓")
        bot.send_message(call.from_user.id, config.othernum)

    elif call.data == "tarifound":
        bot.send_message(call.from_user.id, "Тариф потрібний для:", reply_markup=tarifor())
    elif call.data == "other":
        bot.send_message(call.from_user.id, "Плануєте використовувати для:", reply_markup=nf())

    elif call.data == "phone":
        bot.send_message(call.from_user.id, "Що ви бажаєте?", reply_markup=create())
    elif call.data == "skip":
        bot.send_message(call.from_user.id, "Ви бажаєте користуватися найкращим тарифом, та не обмежувати себе у бажаннях?", reply_markup=best())

    elif call.data == "no/b":
        bot.send_message(call.from_user.id, "Чи бажаєте ви тариф, інтернет, хвилини та смс якого, можуть спільно використовувати ваша сім'я (5 номерів)?", reply_markup=family())
    elif call.data == "yes":
        bot.send_message(call.from_user.id, "Ми маємо для вас 3 варіанти:", reply_markup=family2())


    elif call.data == "no":
        bot.send_message(call.from_user.id, "Ви проводите багато часу з друзями та маєте потребу ділитися з ними інтернетом?", reply_markup=friends())

    elif call.data == "no/f":
        bot.send_message(call.from_user.id, "Ви бажаєте тариф для:", reply_markup=ss())

    elif call.data == "yes/f":
        bot.send_message(call.from_user.id, "Ми маємо для вас такі варіанті, з безкоштовною роздачею інтернету.", reply_markup=friends3())

    elif call.data == "825":
        bot.send_message(call.from_user.id, "Ми маємо 2 економних тарифа з різним наповненням:\n\nСмарт Лайф - 25гб, 120грн\nПросто Лайф - 8гб, 90грн\n\n*Зверніть увагу, студентам знижка 10%!", reply_markup=friends825())
    elif call.data == "ui":
        bot.send_message(call.from_user.id, "Маємо для вас 2 тарифи без обмежень!\n\nВільний Лайф - свобода за розумні гроші\n(Знижка для студентів - 10% 😉)\n\nPlatinum Лайф - 500мб у роумінгу, Хмарне сховище lifebox: 500 ГБ\nТа інші складові Platinum - якості!", reply_markup=friendsui())
    elif call.data == "student":
        bot.send_message(call.from_user.id, "Ви можете отримати студентську знижку за такими тарифами:", reply_markup=student())
    elif call.data == "other/2":
        bot.send_message(call.from_user.id, "Пропонуємо розглянути ці тарифи:", reply_markup=ft())
bot.polling(none_stop=True)
