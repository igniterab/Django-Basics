from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    content = models.TextField()
    mimg = models.ImageField(upload_to='media/')
    #time = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name


    