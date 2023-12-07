from django.db import models
from category.models import Category

class Task(models.Model) :
    title = models.CharField(max_length=50)
    assignDate = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self) :
        return self.title
