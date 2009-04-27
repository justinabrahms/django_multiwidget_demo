from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return "Post: %s" % self.name
