from django.db import models

# Create your models here.
class Test(models.Model):
    test = models.CharField(max_length=20)
    nochange = models.CharField(max_length=20, default="we are set", null=True)

    def __unicode__(self):
        return self.test
    