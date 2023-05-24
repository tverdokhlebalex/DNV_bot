# импорт необходимых библиотек
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# определение класса вина


class Wine:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price


# создание списка вин из меню
wines = [
    # белые вина
    Wine("Хардис Совиньон Блан", "white", 2000),
    Wine("G7 Совиньен Блан", "white", 1900),

    # красные вина
    Wine("Пенедес Азимут", "red", 2500),
    Wine("Конде Отинано Крианца Риоха", "red", 1700),

    # розовые вина
    Wine("Кот Де Гасконь Лаффит Каберне Фран/Марселан", "rose", 1700),
    Wine("Вайнхаус Каннис Португизер", "rose", 1900),

    # игристые вина
    Wine("Херрес Рислинг Дойче Зект", "sparkling", 2900),
    Wine("Просекко Фонте", "sparkling", 1950),

]

# функция для вывода списка вин по предпочтениям гостя


def recommend_wine(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Пожалуйста, укажите тип вина.")
        return

    preference = context.args[0]
    recommended_wines = [wine for wine in wines if wine.type == preference]

    if not recommended_wines:
        update.message.reply_text(
            "К сожалению, мы не можем найти вино этого типа.")
        return

    message = ""
    for wine in recommended_wines:
        message += f"{wine.name}: {wine.price}\n"

    update.message.reply_text(message)

# создание и настройка бота


def main():
    updater = Updater(
        token='6074505625:AAH822pYAU0I66rMI8VHT6nTAuBYPzt5CRg', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('recommend_wine', recommend_wine))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
