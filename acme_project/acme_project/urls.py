from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path('logout/',
         views.LogoutView.as_view(template_name='registration/logged_out.html'),
         name='logout',
         ),
    path('birthday/', include('birthday.urls')),
]
