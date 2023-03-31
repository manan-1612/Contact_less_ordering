"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>/', views.home, name='home'),
    path('menu/<str:id>/', views.menu, name='menu'),
    path('details/<int:delId>/', views.details, name='details'),
    path('<int:id>/bill/', views.bill, name='bill'),
    path('<str:cat>/<str:id>/<str:tid>/', views.south, name='south'),
    path('<str:cat>/<str:orderId>/<str:food_id>', views.additem, name='additem'),
    path('<id>/orderstatus', views.order_status, name='order_status'),
    path('bill/<int:o_id>/<str:price>/pay/',views.payment, name='payment'),
    path('item/<o_id>/<str:f_id>/delete',views.delete_item, name='delete_item'),
    path('modification/<o_id>/<str:f_id>/comment',views.comment, name='comment'),
]
urlpatterns += staticfiles_urlpatterns()