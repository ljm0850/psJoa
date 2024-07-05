from django.db import models

# Create your models here.
class Problem(models.Model):
    problem_num = models.IntegerField(null=False)
    analysis_ai = models.TextField()

