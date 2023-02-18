from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:10]

class blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete= models.CASCADE,
    )
    body=models.TextField()
    
    def __str__(self):
        return self.title
