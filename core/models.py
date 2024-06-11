from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    TITLE_CHOICE = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
    )
    profile_pic = models.ImageField(upload_to='static/images', default='static/images/default.png')
    title = models.CharField(choices=TITLE_CHOICE, max_length=8, default='Student')
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'
        ordering = ['-created_at',]