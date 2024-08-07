from django.urls import path
from .views import ArticleList, ArticleDetail, CommentList, CommentDetail, ArticleComments

urlpatterns = [
  path('articles/', ArticleList.as_view()),
  path('articles/<int:pk>', ArticleDetail.as_view()),
  path('comments/', CommentList.as_view()),
  path('comments/<int:pk>', CommentDetail.as_view()),
  path('articles/<int:pk>/comments', ArticleComments.as_view())
  ]