from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article

@api_view(['POST', 'GET'])
def add_article(request):
    if request.method == "POST":
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response({
                "status": "success",
                "message": "Article posted successfully",
                "data": article
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "Bad Request",
            "message": "Article did not post",
            "errors": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        try:
            articles = Article.objects.all()
            if not articles:
                return Response({
                    "status": "error",
                    "message": "No articles found"
                }, status=status.HTTP_404_NOT_FOUND)
                
            serializer = ArticleSerializer(articles, many=True)
            return Response({
                "status": "success",
                "message": "Articles fetched successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


    