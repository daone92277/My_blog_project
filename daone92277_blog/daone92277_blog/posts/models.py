from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    body = models.TextField()

#   how to shorten the date time attribute
    # def pub_date_pretty(self):
    #     return self.pub_date.strftime("%b %d %y")

# how to shorten the lenght of the body posts
    def body_length(self):
        return self.body[:100]

    def title_fix(self):
        return self.title.title()