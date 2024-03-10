from django.db import models

from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
        # related_name : 연결된 객체에서 하위 객체의 목록을 부를 때 사용할 이름.
        # 이 모델에서는 어떤 유저가 작성한 글을 불러 올 때는 유저 객체에 user_photos 속성을 참조하면된다.
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)   # auto_now_add : 객체가 추가될 때 자동으로 값을 설정한다.
    updated = models.DateTimeField(auto_now=True)       # auto_now : 객체가 수정될 때마다 자동으로 값을 설정한다.

    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])