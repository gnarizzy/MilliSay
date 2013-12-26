from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now()) #make default now, set timzeone for east coast
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    words = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

