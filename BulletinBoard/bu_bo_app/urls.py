from django.urls import path
from .views import (ArticlesList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, CommentCreate,
                    CommentDetail, CommentUpdate, CommentDelete, PrivateArticleCommentList, comment_accept, comment_deny)


urlpatterns = [
   path('', ArticlesList.as_view(), name='articles_list'),
   path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

   path('privatecommentlist/', PrivateArticleCommentList.as_view(), name='private_comment_list'),  # личная страница
   path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'), # создание коммента
   path('privatecommentlist/<int:pk>/', CommentDetail.as_view(), name='comment_detail'), # детали коммента
   path('privatecommentlist/<int:pk>/accept', comment_accept, name='comment_accept'),# коммент принят
   path('privatecommentlist/<int:pk>/deny', comment_deny, name='comment_deny'),# коммент не принят
   path('privatecommentlist/<int:pk>/delete', CommentDelete.as_view(), name='comment_delete'), # удаление коммента
   path('privatecommentlist/<int:pk>/edit', CommentUpdate.as_view(), name='comment_edit'),  # изменение коммента

]











