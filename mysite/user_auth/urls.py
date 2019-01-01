from django.urls import path, include
from .views import login_page, login_view

urlpatterns = [
    path('login/', login_page, name='login'),
    path('do_login/', login_view, name='do_login'),
]
