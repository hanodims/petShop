"""pet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from  petshop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.pet_list, name='pet-list'),
    path('detail/<int:pet_id>', views.pet_detail, name='pet-detail'),
    path('pet/<int:pet_id>/update/', views.pet_update, name='pet-update'),
    path('create/', views.pet_create, name='pet-create'),
        path('pet/<int:pet_id>/delete/', views.pet_delete, name='pet-delete'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
