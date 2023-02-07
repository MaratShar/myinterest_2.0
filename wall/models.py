from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    likes = models.IntegerField(default = 0)
    discription = models.TextField(null = True)

    def __str__(self):
        return f'{self.author} {self.date}'
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'




