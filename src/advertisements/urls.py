"""advertisements URL Configuration

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
from advertisements.app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category', views.CategoryList.as_view(),
         name='return all categories ordered by ordering field or POST a category'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='manipulates a single category'),
    path('offers', views.OfferList.as_view(),
         name='return all offers with columns ID, title, price and category ID - optionally accepts category ID as a query parameter (named category) or POST a category'),
    path('offers/<int:pk>', views.OfferDetail.as_view(), name='manipulates a single offer'),
]
