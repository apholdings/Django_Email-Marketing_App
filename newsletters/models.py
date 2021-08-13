from django.db import models

# Create your models here.

class NewsletterUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body=models.TextField(blank=True, null=True)
    email = models.ManyToManyField(NewsletterUser)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name