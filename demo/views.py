from rest_framework import generics
from .models import Articles, Comments
from .serializer import ArticleSerializer, CommentSerializer

class CommentList(generics.ListCreateAPIView):
  serializer_class = CommentSerializer

  def get_queryset(self):
    querySet = Comments.objects.all()
    article = self.request.query_params.get('article')
    if article is not None:
      querySet = querySet.filter(article=article)
    return querySet

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Comments.objects.all()
   serializer_class = CommentSerializer

class ArticleList(generics.ListCreateAPIView):
  queryset = Articles.objects.all()
  serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Articles.objects.all()
  serializer_class = ArticleSerializer

class ArticleComments(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['pk']
        return Comments.objects.filter(article_id=article_id)