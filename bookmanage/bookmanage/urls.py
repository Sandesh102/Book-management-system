"""
URL configuration for bookmanage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookapp.views import *
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',book,name='book'),
    path('book/',book,name='book'),
    path('delete_book/<id>/',delete_book,name='delete_book'),
    path('update_book/<id>/',update_book,name='update_book'),
    path('login/',login_page,name="login_page"),
    path('register/',register_page,name="register_page"),
    path('logout/',logout_page,name="logout_page"),
    
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
  document_root=settings.MEDIA_ROOT)
urlpatterns +=staticfiles_urlpatterns()
