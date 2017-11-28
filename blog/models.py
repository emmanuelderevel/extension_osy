from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Infos(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    url = models.CharField(max_length=100)

    def __str__(self):
        login="Username : {0}, Password : {1}, URL : {2}".format(self.username, self.password, self.url)
        return login

class Infos_string(models.Model):
    infos = models.CharField(max_length=200)

    def __str__(self):
        infos="Infos : {}".format(self.infos)
        return infos

