from django.db import models
from django.conf import settings
from problems.models import Problem

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem_num = models.ForeignKey(Problem,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    code = models.TextField()
    ai_logic = models.TextField()
    ai_code = models.TextField()
    language = models.CharField(max_length=30)
    is_public = models.BooleanField(default=True)
    is_ai_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title