from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
import main.views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/',include('main.urls') ),
    path('', main.views.land),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
