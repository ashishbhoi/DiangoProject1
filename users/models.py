import os
from django.db import models
from django.contrib.auth.models import User
from google.oauth2 import service_account
from PIL import Image

GS_CREDENTIALS = service_account.Credentials.from_service_account_file('users/google-storage-api.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './users/google-storage-api.json'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
