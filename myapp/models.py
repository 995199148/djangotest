from django.db import models

# Create your models here.
class clientnum(models.Model):
    cid = models.IntegerField(null=True, verbose_name="客户端id")
    num = models.IntegerField(null=True, verbose_name="分数")