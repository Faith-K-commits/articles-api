from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from django.db.models import Q

@api_view(['POST', 'GET'])
def articles(request):
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Article posted successfully",
                "data": serializer.data
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


@api_view(['GET'])
def get_articles_by_language(request, language):
    try:
        # Filter case insensitively
        articles = Article.objects.filter(programming_language__iexact=language)
        if not articles:
            return Response({
                "status": "error",
                "message": f"no {language} articles found",
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(articles, many=True)
        return Response({
            "status": "success",
            "message": f"{language} articles retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "status": "errors",
            "message": str(e),
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def search_articles(request):
    keywords = request.GET.get('keywords', '')
    language = request.GET.get('language', '')
    tags = request.GET.get('tags', '')
    
    queryset = Article.objects.all()
    if keywords:
        queryset = queryset.filter(
            Q(title__icontains=keywords) | Q(description__icontains=keywords)
        )
        
    if language:
        queryset = queryset.filter(programming_language__iexact=language)
    
    if tags:
        tags_list = tags.split(',')
        for tag in tags_list:
            queryset = queryset.filter(tags__icontains=tag.strip())
            
    serializer = ArticleSerializer(queryset, many=True)
    return Response({
        'status': 'success',
        'message': 'Articles retrieved successfully',
        'data': serializer.data
    }, status=status.HTTP_200_OK)
    
@api_view(['PATCH'])
def update_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({
            "error": "Item not found"
        }, status=status.HTTP_404_NOT_FOUND)
        
    serializer = ArticleSerializer(article, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        
        return Response({
            "status": "success",
            "message": "Article updated successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE'])
def delete_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response({'message': 'Article deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Article.DoesNotExist:
        return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)