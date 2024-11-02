from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book, CommentModel
from .forms import SignUp, CustomUserLogin

# Create your views here.






def pair_form(request, pk):
    if request.method == "POST":
        if pk == 0:
            request


def marks_for_book(book: Book):
    comments = CommentModel.objects.filter(post=book)  # получение всех комментов для книги
    marks = []
    for comment in comments:
        marks.append(comment.marks)
    # словарь в формате (название книги: [кол-во комментов, оценки, объект книги, комментарии])
    return [len(comments), marks, book, comments]

def marks_for_books(books):
    comments_marks = {}
    for i in books:  # перебор книг
        mark_book = marks_for_book(i)
        comments_marks[mark_book[2].name_book] = mark_book

    return comments_marks

def recom_return(comments_marks: dict):
    list_good_recom = []
    for name_film, marks_test in comments_marks.items():
        if marks_test[0] >= 100 and sum(marks_test[1]) / len(
                marks_test[1]) >= 4.4:  # система рекомендации: если у книги
            list_good_recom.append(marks_test[2])
    return list_good_recom


def home(request):
    books = Book.objects.all()                # обычная домашняя страница

    return render(request, 'html/main/index.html', {'books': books, 'url': 'index'})


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    test_new = marks_for_book(book)
    context = {
        "book": book,
        'url': 'index',
        'marks': test_new,
    }
    return render(request, 'html/detail/detail.html', context)

def recomen(request):
    if request.user.is_authenticated:
        pass
    books = Book.objects.all()               # получение всех книг
    marks = marks_for_books(books)

    list_recom = recom_return(marks)

    if len(list_recom) == 0:
        return render(request, 'html/recom/null_recom.html')
    return render(request, 'html/recom/recomenndation.html', {'recoms': list_recom, 'url': 'recom'})


def about(request):
    return render(request, 'html/main/about.html')


def buying_book(request, slug):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, slug=slug)
        return HttpResponse("Вы зарегистрированы")
    else:
        books = Book.objects.all()  # обычная домашняя страница
        messages.success(request, 'Вы незарегистрированы')
        return 


def subscription(request):
    return render(request, 'html/buying/subscription.html')


def account(request):
    user = request.user
    if user.is_authenticated:
        print(user.books)
        return render(request, 'html/account/myAccount.html')
    else:
        return signup(request)




def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUp()
    return render(request, 'html/registration/signup.html', {'form':form})






def login_view(request):

    if request.method == 'POST':
        form = CustomUserLogin(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                books = Book.objects.all()  # обычная домашняя страница

                return render(request, 'html/main/index.html', {'books': books, 'url': 'index'})
            else:
                books = Book.objects.all()  # обычная домашняя страница

                return render(request, 'html/main/index.html', {'books': books, 'url': 'index'})
        else:
            return render(request, '', {'form': form})




def logout_view(request):
    logout(request)
    response = redirect('/')
    return response