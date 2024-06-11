from django.db import models
from core.models import *


class Blog(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='available')

    POSTED_CHOICES = (
        ('available', 'available'),
        ('unavailable', 'unavailable'),
    )

    favourites = models.ManyToManyField(User, related_name='Property', default=None, blank=True)
    created_by = models.ForeignKey(Profile, related_name="blog", on_delete=models.CASCADE)
    status = models.CharField(choices=POSTED_CHOICES, max_length=12, default='available')
    img = models.ImageField(upload_to='static/images/blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    body = models.TextField()
    objects = models.Manager()
    newmanager = NewManager()

    
        
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        
        
        
class Comments(models.Model):
    sent_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'
        ordering = ['-sent_at']
        