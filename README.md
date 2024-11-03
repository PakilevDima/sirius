# Задание второго этапа
В качестве интерфейса - тг бот

В качестве моделей - модели из директории [summarization](https://github.com/PakilevDima/sirius/tree/main/summarization)

## [summarization](https://github.com/PakilevDima/sirius/tree/main/summarization)
В этом модуле содержатся 6 моделей суммаризации
- [kl_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/kl_summarization.py) -
суммаризация текста с помощью алгоритма Kl
- [lex_rank_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/lex_rank_summarization.py) - 
суммаризация текста с помощью алгорима LexRank
- [llana_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/llana_summarization.py) - 
суммаризация текста с помощью большой языковой модели Llama
- [lsa_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/lsa_summarization.py) - 
суммаризация текста с помощью алгоритма LSA
- [lunh_rank_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/lunh_rank_summarization.py) -
суммаризация текста с помощью алгоритма LunhRank
- [text_rank_summarization.py](https://github.com/PakilevDima/sirius/blob/main/summarization/text_rank_summarization.py) - 
суммаризация текста с помощью алгоритма TextRank
## Интрефейс
В файле [bot.py](https://github.com/PakilevDima/sirius/blob/main/bot.py) содержится интерфейс для взаимодействия с 
пользователем. Часть функционала бота является функционалом 1-ого задания


## Установка библиотек:
1. `pip install django` - для установки django

2. `pip install sumy` - для установки sumy

3. `pip install pytelegrambotapi` - для установки telebot

4. `pip install requests` - для установки requests

5. `pip install selenium` - для установки selenium

Для установки llama-cpp смотреть по [ссылке](https://github.com/ggerganov/llama.cpp)

Модель [llama](https://drive.google.com/file/d/1wq8FYFJ2Z03269Qi8z_ECJwcG0Xrnewd/view?usp=sharing)


---

#  (Эта информация о прототипе (разрабатывался на первом этапе, содержит доп. функциональность) Прототип (sirius)
В данном проекте предоставлены сайт системы, telegram-бот и модели для суммаризации текста

В директории [sirius_website](https://github.com/PakilevDima/sirius/tree/main/sirius_website) находится сайт, созданный 
при помощи django-rest-framework. Для запуска сайта необходимо скачать django, python и репозиторий с сайтом. Затем 
необходимо перейти в директорию с **manage.py** и в коносоли прописать `python manage.py runserver`.

В директории [summarization](https://github.com/PakilevDima/sirius/tree/main/summarization) находятся файлы моделей для 
суммаризации текста, 5 из которых предоставляют суммаризацию на основе 5 разных моделей для суммаризации, а 6-я 
предоставляет работу с большой языковой моделью 'Llama'. Пользователю на выбор даются эти модели. Модель llama работает 
с помощью библиотеки llama_cpp, а остальные модели с помощью библиотеки sumy

[bot.py](https://github.com/PakilevDima/sirius/blob/main/bot.py) - файл работы Telegram-бота, который позволяет выполнять 
суммаризацию текста моделями из директории
[summarization](https://github.com/PakilevDima/sirius/tree/main/summarization). Для работы использует библиотеку telebot.

[parser.py](https://github.com/PakilevDima/sirius/blob/main/parser.py) - 
парсер [сайта](https://ilibrary.ru/) с книгами. 
Для работы используется selenium.
