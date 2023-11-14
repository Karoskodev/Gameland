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
    

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name


class Entry(models.Model):

    TITLES = [
        ('CodeWarrior', 'CodeWarrior'),
        ('SyntaxSlayer', 'SyntaxSlayer'),
        ('LogicChampion', 'LogicChampion'),
        ('ByteBrawler', 'ByteBrawler'),
        ('BinaryNinja', 'BinaryNinja'),
        ('AlgorithmMaster', 'AlgorithmMaster'),
        ('PythonWhistler', 'PythonWhistler'),
        ('DjangoEater', 'DjangoEater'),
        ('JavaDriver', 'JavaDriver'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='entries')
    user = models.ForeignKey(User, related_name='entries', blank=True, null=True, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50,default="", choices=TITLES)
    clan = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Player"

    def __str__(self):
        return f"{self.nick_name} clan:{self.clan}"
