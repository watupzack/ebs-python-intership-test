from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField('Enabled', default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
