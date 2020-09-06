"""BuildingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from DesignApp.views import home_view,DesignApp_view,UserList_view,BuildingCreateView,BuildingList_view
from DesignApp.views import Building_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('Buildings/forms',BuildingCreateView),
    path('Users/<int:user_id>/', DesignApp_view),
    path('Users/', UserList_view),
    path('Buildings/', Building_view),
    path('BuildingsList/', BuildingList_view),


]
