from django.urls import path, include
from . import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('reset_pw/', views.reset_pw, name='reset_pw'),
    path('join/', views.join, name='join'),
    path('join_select/',views.join_select, name ='join_select'),
    path('join_mentor/',views.join_mentor, name ='join_mentor'),
    path('join_mentee/',views.join_mentee, name ='join_mentee'),
    path('community',views.community, name='community'),
    path('new_writing/',views.new_writing, name = 'new_writing'),
    path('community_post/',views.community_post,name='community_post'),
    path('logout/', views.logout, name='logout'),
    # path('board/', views.board, name='board'),
    # path('board/board_write/', views.board_write, name='board_write'),
    path('cover_letter/',views.cover_letter,name='cover_letter'),
    path('board/board_detail/<int:boardid>/', views.board_detail, name='board_detail'),
    path('board/board_detail/<int:boardid>/delete/', views.board_delete, name='board_delete'),
    path('board/board_detail/<int:boardid>/modify/', views.board_modify, name='board_modify'),
    path('new_comment/<int:boardid>', views.new_comment, name='new_comment'),
    path('update_comment/<int:boardid>/<int:commentid>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:boardid>/<int:commentid>', views.delete_comment, name='delete_comment'),
   
]