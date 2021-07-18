"""project17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app17 import views
from django.conf.urls.static import static
from project17 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex, name="home"),
    path('view_all/', views.showAll, name="view_all"),
    path('delete/<int:number>', views.showDelete, name="delete_data"),
    path('updata_data/<int:number>', views.showUpdatte, name="update_data")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
