from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('recomenndation', views.recomen, name='recomen'),
    path('about', views.about, name='about'),
    path('subscription', views.subscription, name='sub'),
    path('paying', views.pair_form, name='pay'),
    path("signup/", views.signup, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='html/registration/login.html'),name='login'),
    path('acc/', views.account, name='acc'),
    path('detail/buying/book/<slug:slug>', views.buying_book, name='book_buy')
]