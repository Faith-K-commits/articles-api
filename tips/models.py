from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    programming_language = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
