from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField() #make default now, set timzeone for east coast
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    words = models.IntegerField(default=0)
    is_top = models.BooleanField(default=False)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

