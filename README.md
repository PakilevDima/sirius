# sirius
В данном проекте предоставлены сайт системы, telegram-бот и модели для суммаризации текста

В репозитории 'sirius_website' находится сайт, созданный при помощи django-rest-framework. Для запуска сайта необходимо скачать django, python и репозиторий с сайтом. Затем необходимо перейти в репозиторий с 'manage.py' и в коносоли прописать 'python manage.py runserver'.

В репозитории 'summarization' находятся файлы моделей для суммаризации текста, 5 из которых предоставляют суммаризацию на основе 5 разных моделей для суммаризации, а 6 предоставляет работу с большой языковой моделью 'Llana'. Пользователю на выбор даются эти модели. Модель llana работает с помощью библиотеки llana_cpp, а остальные модели с помощью библиотеки sumy

bot.py - файл работы Telegram-бота, который позволяет выполнять суммаризацию текста моделями из репозитория 'summarization'. Для работы использует библиотеку telebot.
parser.py - парсер сайта https://ilibrary.ru/ с книгами. Для работы используется selenium.




# 1. Установка библиотек:
pip install django - для установки django

pip install sumy - для установки sumy

pip install pytelegrambotapi - для установки telebot

pip install requests - для установки requests

Для установки llana-cpp смотреть по [ссылке](https://github.com/ggerganov/llama.cpp)

Модель [llana ] (https://drive.google.com/file/d/1wq8FYFJ2Z03269Qi8z_ECJwcG0Xrnewd/view?usp=sharing)
