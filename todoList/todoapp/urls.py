from django.urls import path
from . import views

urlpatterns = [
    path('', views.alltodos, name='alltodos'),
    path('delete<int:pk>', views.Delete, name='delete'),
    path('update<int:pk>', views.Update, name='update'),
]
