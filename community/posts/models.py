from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import misaka #markdown files
import os
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=264,unique=True)
    date = models.DateField(default=timezone.now)
    file = models.FileField(null=True,blank=True,upload_to='files')
    content = models.TextField()
    content_html = models.TextField(editable=False)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.content_html = misaka.html(self.content)
        super().save(*args,**kwargs)

    def get_file_extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse('posts:post',kwargs={'pk':self.pk} )

    class Meta:
        ordering = ['-date']
        unique_together = ['user','title']
