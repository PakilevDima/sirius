
import telebot  # Импортируем все функции telebot
from telebot import types  # Импортируем функцию telebot.types
import time
import random
import os
from summarization.kl_summarization import sum_text as kl_sum
from summarization.lex_rank_summarization import sum_text as lex_rank_sum
from summarization.llana_summarization import llana_model as llana_sum
from summarization.lsa_summarization import sum_text as lsa_sum
from summarization.lunh_rank_summarization import sum_text as lunh_rank_sum
from summarization.text_rank_summarization import sum_text as text_rank_sum


def check_user_sverhrazum(username):       # проверка пользователя на наличие подписки

    return "yes"

bot = telebot.TeleBot(
    '7123980630:AAEvmMkstfxYy90wJbDUH7G7LdVfFYYPIXo'
)
# bot - это теперь telebot.Telebot. В скобках я указываю токен бота






@bot.message_handler(commands=['start'])
# Команда /start является стартовой для всех ботов в Telegram. Отсюда и начинается пользование нашего бота.
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сообщить о ошибке')
    markup.row(btn1)
    btn3 = types.KeyboardButton('Прочитать книгу')
    markup.row(btn3)
    btn4 = types.KeyboardButton('Новинки')
    markup.row(btn4)
    btn5 = types.KeyboardButton('Помощь в использовании бота')
    markup.row(btn5)
    btn6 = types.KeyboardButton("Сжать текст")
    markup.row(btn6)
    bot.send_message(message.chat.id,
                     f'Здравствуйте, {message.from_user.username} +'
                     f'! Этот бот создан для программы Сириус.ИИ, и некоторые функции пока могут не работать.',
                     reply_markup=markup)

class BotMethod:
    def book(self, message):
        # После ввода команды бот проверит, а оформили ли вы подписку вообще, если да - то продолжит выполнение.
        # Если нет - то попросит оформить (Не, ну а что? Любой труд должен оплачиваться).
        if check_user_sverhrazum(message.from_user.username) == "yes":
            bot.send_message(message.chat.id,
                             'Хорошо. Какую книгу хотите прочесть? Например: А. С. Пушкин - "Дубровский"')
            # бот отправляет сообщение
            bot.register_next_step_handler(message, self.open_book)
        elif check_user_sverhrazum(message.from_user.username) == "no":
            bot.send_message(message.chat.id,
                             'Вы не оформили подписку "СВЕРХРАЗУМ". Если подписка оформлена, то привяжите ваш аккаунт ' +
                             'Telegram к аккаунту сайта. Оформить можно на сайте: <URL сайта>'
                             )


    def open_book(self, message):
        a = random.randint(5, 20)
        bot.reply_to(message, 'Хорошо. Скоро будет открыто окно с сайтом, где будет запрашиваемая книга.')
        time.sleep(a)
        a1 = random.randint(0, 1)
        if a1 == 0:
            bot.send_message(message.chat.id, 'Функция временно не работает. Извините.')
        if a1 == 1:
            bot.send_message(message.chat.id, "Упс. Произошла внутренняя ошибка сервера. Повторите запрос позже")


    def audio_book(self, message):
        if check_user_sverhrazum(message.from_user.username) == "yes":
            # бот отправляет сообщение
            bot.send_message(message.chat.id,
                             'Хорошо. Какую книгу хотите прослушать? Например: А. С. Пушкин - "Сказка о рыбаке и рыбке"')

            bot.register_next_step_handler(message, self.open_audiobook)

        else:
            bot.send_message(
                'Вы не оформили подписку "СВЕРХРАЗУМ". Если подписка оформлена, ' +
                'то привяжите ваш аккаунт Telegram к аккаунту сайта. Оформить можно на сайте: <URL сайта>'
            )

    def open_audiobook(self, message):
        a = random.randint(5, 20)
        bot.reply_to(message, 'Хорошо. Скоро будет открыто окно с сайтом, где будет запрашиваемая аудиокнига.')
        time.sleep(a)
        a1 = random.randint(0, 1)
        if a1 == 0:
            bot.send_message(message.chat.id, 'Функция временно не работает. Извините.')
        if a1 == 1:
            bot.send_message(message.chat.id, "Упс. Произошла внутренняя ошибка сервера. Повторите запрос позже")

    def bug_report(self, message):
        # Бот попросит прикрепить описание проблемы и, по желанию, прикрепить фото или видео
        #
        bot.send_message(message.chat.id,
                         'Вас приветствует тех. поддержка. Опишите проблему. По желанию можно прикрепить фото, видео.')
        bot.send_message(message.chat.id,
                         'Например: "Здравствуйте! У меня не работает часть функций бота. Пишит: Функция временно не ' +
                         'работает. Сможете это пофиксить?"')
        bot.register_next_step_handler(message, self.bug_report_message)

    def bug_report_message(self, message):
        bot.reply_to(message, 'Спасибо! Наши специалисты рассмотрят проблему в ближайшее время.')

    def new_books(self, message):
        bot.send_message(message.chat.id, 'Функция временно не работает. Извините.')

    def help_bot(self, message):
        bot.send_message(message.chat.id,
                         'Это бот, которого разработала команда #2. Разработан для программы Сириус.ИИ по техническому заданию от Sber.AI')
        bot.send_message(message.chat.id,
                         'Через бота вы можете читать книги, слушать их, и главное - это нейро-иллюстрации, ' +
                         'сгенерированный Kandinsky, чтобы не было скучно. Прослушать аудиокнигу: ' +
                         '/audio_book, прочитать книгу: /book')
        bot.send_message(message.chat.id, 'Нужны свежие новинки? Без проблем. Введите команду /new_books')
        bot.send_message(message.chat.id,
                         'Нашли баг или ошибку? Нужно решить проблему? Введите команду /bug_report и опишите проблему. Вам точно помогут.')

        bot.send_message(message.chat.id,
                         'ВНИМАНИЕ! Для пользования ботом (за исключением /help ,/sub и /bug_report), нужно оформить +'
                         'подписку "СВЕРХРАЗУМ", иначе бот работать не будет. Если подписка оформлена, +'
                         'то привяжите ваш аккаунт Telegram к аккаунту сайта.')


src = ''

@bot.message_handler(content_types=['document'])
def get_text_sum(message):
    global src
    try:

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        if message.document.file_name[-3:] == 'txt':

            src = 'summarization_files/' + f'{message.chat.id}/' + message.document.file_name
            if os.path.exists('summarization_files/' + f'{message.chat.id}') is False:
                if os.path.exists('summarization_files') is False:
                    os.mkdir('summarization_files')
                os.chdir('summarization_files')
                os.mkdir(f'{message.chat.id}')
            with open(src, 'w') as new_file:
                pass
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)


            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('LSA метод')
            markup.row(btn1)
            btn2 = types.InlineKeyboardButton('Lex Rank метод')
            markup.row(btn2)
            btn3 = types.KeyboardButton('KL метод')
            markup.row(btn3)
            btn4 = types.InlineKeyboardButton('Text Rank метод')
            markup.row(btn4)
            btn5 = types.KeyboardButton('Lunh Rank метод')
            markup.row(btn5)
            btn6 = types.InlineKeyboardButton('С помощью модели Llana')
            markup.row(btn6)
            bot.send_message(message.chat.id,
                             'Выберите как сжать текст',
                             reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'Вы отправили не txt-файл')
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Извините. Возникла ошибка при обработке файла')



def sum_text(message):
    if check_user_sverhrazum(message.from_user.username) == "yes":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Сжать до 5 предложений')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton('Сжать до маленького абзаца')
        markup.row(btn2)
        bot.send_message(message.chat.id,
                         'Выберите категорию сжатия текста',
                         reply_markup=markup)

@bot.message_handler(commands=['LSA метод',
                               'Lex Rank метод',
                               'KL метод',
                               'Text Rank метод',
                               'Lunh метод',
                               'С помощью модели Llana',
                               ]
                     )

def get_sentences(message):
    pass


sentences = None
@bot.message_handler(content_types=['text'])
def handler(message):
    global sentences
    bot_class = BotMethod()
    if message.text == "Новинки":
        bot_class.new_books(message)
    if message.text == "Сообщить о ошибке":
        bot_class.bug_report(message)
    if message.text == "Прочитать книгу":
        bot_class.book(message)
    if message.text == "Помощь в использовании бота":
        bot_class.help_bot(message)
    if message.text == "Сжать текст":
        sum_text(message)
    if message.text == "Сжать до 5 предложений":
        sentences = 5
        bot.send_message(message.chat.id, 'Отправьте файл с текстом для сжатия')
    if message.text == 'Сжать до маленького абзаца':
        sentences = 30
        bot.send_message(message.chat.id, 'Отправьте файл с текстом для сжатия')

    if message.text == 'LSA метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(lsa_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'Lex Rank метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(lex_rank_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'KL метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(kl_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'Text Rank метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(text_rank_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'Lunh Rank метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(lunh_rank_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'Text Rank метод':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:
                string_input = ''
                with open(src, 'r', encoding='cp1251') as file_input:
                    for i in file_input.readlines():
                        string_input += i
                file_time.write(text_rank_sum(sentences, string_input))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))

    if message.text == 'С помощью модели Llana':
        if sentences is None:
            bot.send_message(message.chat.id,
                             'Вы нарушили порядок инструкции. Пожалуйста, перезапустите бота и сделайте все заново'
                             )
        else:
            with open('1.txt', 'w') as file_time:

                file_time.write(llana_sum(src, sentences))
            bot.send_document(message.chat.id, open('1.txt', 'rb'))


bot.polling(none_stop=True)  # Работа бота постаянная, пока программа работает

