from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class TypeBook(models.Model):
    name_type = models.CharField(max_length=50, verbose_name='Название жанра')

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

SUBSCRIBE_VADIDATION = (
    ('начинающий', 'НАЧИНАЮЩИЙ'),
    ('читающий', 'ЧИТАЮЩИЙ'),
    ('библиотекарь', 'БИБЛИОТЕКАРЬ'),
    ('сверхразум', 'СВЕРХРАЗУМ'),
)

TYPE_USER = (
    ('читатель', 'ЧИТАТЕЛЬ'),
    ('автор', 'АВТОР')
)




class Book(models.Model):
    name_book = models.CharField(max_length=100, verbose_name='Название книги')
    author_book = models.CharField(max_length=50, verbose_name='Автор')
    type_book = models.ManyToManyField(TypeBook, verbose_name="Жанр", related_name="type_book")
    image_book = models.ImageField(blank=True, verbose_name='Обложка',upload_to=f'book/files/{id(name_book)}')
    description = models.TextField(verbose_name='Описание')
    isbn = models.IntegerField(max_length=14, verbose_name='ISBN')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    book_file = models.FileField(upload_to=f'book/files/{id(name_book)}',
                                 verbose_name='Файл книги',
                                 validators=[FileExtensionValidator(['txt', 'docx'])])

    def __str__(self):
        return self.name_book

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class CustomUser(AbstractUser):
    name = models.CharField(max_length=40, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    subscribe = models.CharField(max_length=16, choices=SUBSCRIBE_VADIDATION, default='начинающий')
    books = models.ManyToManyField(Book, verbose_name='Купленные книги', blank=True, default=None)
    type_user = models.CharField(max_length=10, verbose_name='Тип пользователя', choices=TYPE_USER, default='читатель')


    def __str__(self):
        return self.username


class CommentModel(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    post = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Пост",
        related_name="comments",
    )
    marks = models.IntegerField()
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.user} к посту {self.post}"

