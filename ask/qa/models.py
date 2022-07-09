from django.db import models 
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/post/%d/' % self.pk
    class Meta:
        db_table = 'blogposts'
        ordering = ['-creation_date']
