from django.shortcuts import render
from articles.models import Article
from rest_framework.response import Response
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


       

