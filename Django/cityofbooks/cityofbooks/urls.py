
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from cityapp.views import index, loginPage, register, logoutUser, book1, book2, book3, book4, book5, book6, book7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name = "homepage"),
    path('login/', loginPage, name = "login"),
    path('logout/', logoutUser, name = "logout"),
    path('register/', register, name = "register"),
    path('book1/', book1, name = "book1"),
    path('book2/', book2, name = "book2"),
    path('book3/', book3, name = "book3"),
    path('book4/', book4, name = "book4"),
    path('book5/', book5, name = "book5"),
    path('book6/', book6, name = "book6"),
    path('book7/', book7, name = "book7"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)