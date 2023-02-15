from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e %Y')

