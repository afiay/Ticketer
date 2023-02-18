from calendar import Calendar
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse 
from django.contrib.auth.models import User
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Event(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=30) 
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='event_posts')
    description = models.TextField() 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
	        return reverse('event_posts')
    
