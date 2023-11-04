from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField()
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='event_likes', blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Entry(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='entries')
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_entries')
    nick_name = models.CharField(max_length=50)
    clan = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.nick_name} clan:{self.clan}"
