from django.db import models
from django.db import models


class Post(models.Model):
    PersonName= models.CharField(max_length=300, unique=False)
    SweetName= models.TextField()
    Number=models.IntegerField(default=1)
    