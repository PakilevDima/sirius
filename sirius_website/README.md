# Сайт
В данной директории находится сайт для первого задания. Сайт написан с помощью django-rest-framowork. Проект содержит 2
директории: [client](https://github.com/PakilevDima/sirius/tree/main/sirius_website/client) и 
[sirius_website](https://github.com/PakilevDima/sirius/tree/main/sirius_website/sirius_website)

## client
[client](https://github.com/PakilevDima/sirius/tree/main/sirius_website/client) - приложение, которое реализует
взаимодействие с пользователями. Содержит 
- [модели](https://github.com/PakilevDima/sirius/blob/main/sirius_website/client/models.py)
для базы данных. 
- [страница администрирования](https://github.com/PakilevDima/sirius/blob/main/sirius_website/client/admin.py)
- [формы](https://github.com/PakilevDima/sirius/blob/main/sirius_website/client/forms.py) - для внесения и получения данных
из базы данных
- [views](https://github.com/PakilevDima/sirius/blob/main/sirius_website/client/views.py) - для получения данных из базы
данных с последующей передачей в html-код

## sirius_website
[sirius_website](https://github.com/PakilevDima/sirius/tree/main/sirius_website/sirius_website) содержит системные файлы,
необходимые для работы сайта, такие как [settings.py](https://github.com/PakilevDima/sirius/blob/main/sirius_website/sirius_website/settings.py)
и [urls.py](https://github.com/PakilevDima/sirius/blob/main/sirius_website/sirius_website/urls.py).

## media
[media](https://github.com/PakilevDima/sirius/tree/main/sirius_website/media) - хранит файлы книг, такие как сами книги, их
обложки и тд. 

## db.sqlite3
[db.sqlite3](https://github.com/PakilevDima/sirius/blob/main/sirius_website/db.sqlite3) - это база данных для хранения данных сайта

## manage.py
[manage.py](https://github.com/PakilevDima/sirius/blob/main/sirius_website/manage.py) - системный файл для работы сайта.
НЕ РЕКОМЕНДУЕТСЯ ЕГО ИЗМЕНЯТЬ

