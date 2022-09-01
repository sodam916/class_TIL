from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),

    #게시글 생성/articles/new
    path('new/', views.new, name = 'new'),
    
    path('create/', views.create, name = 'create'),
    #게시글 상세 조회 /articles/글번호(pk)/,/ articles/2/
    #path 컨버터
    path('<int:pk>/', views.detail, name = 'detail'),
    #delete
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    #게시글 수정 / articles/글번호(pk)/update

    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]