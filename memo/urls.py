from django.urls import path
from . import views

app_name = 'memo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_memo, name='add_memo'),
    path('detail/<int:memo_id>/', views.detail, name='detail'),
    path('del/<int:memo_id>/', views.del_memo, name='del_memo'),
    path('mod/<int:memo_id>/', views.mod_memo, name='mod_memo'),
]