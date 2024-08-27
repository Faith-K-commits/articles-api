from django.test import TestCase
from rest_framework.test import APIClient
from .models import Tag, Article
from rest_framework import status

class ArticleModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Python")
        self.article = Article.objects.create(
            title="Test Article",
            description="This is a test article.",
            programming_language="Python"
        )
        self.article.tags.add(self.tag)

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.description, "This is a test article.")
        self.assertEqual(self.article.programming_language, "Python")
        self.assertIn(self.tag, self.article.tags.all())

    def test_article_str(self):
        self.assertEqual(str(self.article), "Test Article")
        
class ArticleAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name="Python")
        self.article = Article.objects.create(
            title="Test Article",
            description="This is a test article.",
            programming_language="Python"
        )
        self.article.tags.add(self.tag)
    
    def test_create_article(self):
        data = {
            "title": "New Article",
            "description": "This is a new article.",
            "programming_language": "Python",
            "tags_input": "Python, Django"
        }
        response = self.client.post('/api/articles/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['title'], "New Article")
    
    def test_get_all_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        
    def test_get_articles_by_language(self):
        response = self.client.get('/api/articles/language/Python/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
    
    def test_search_articles(self):
        response = self.client.get('/api/articles/search/', {'keywords': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        
    def test_update_article(self):
        data = {"title": "Updated title"}
        response = self.client.patch(f'/api/articles/{self.article.id}/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['title'], "Updated title")
    
    def test_delete_article(self):
        response = self.client.delete(f'/api/articles/{self.article.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())
        
        