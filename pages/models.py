from django.db import models

class Team(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link=models.URLField(max_length=100)
    twitter_link=models.URLField(max_length=100)
    google_plus_link=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
